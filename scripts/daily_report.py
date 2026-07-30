#!/usr/bin/env python3
"""
美股日报生成器 - 使用 DeepSeek 直接评分新闻并生成报告
"""
import feedparser, json, os, re, sys
from html import unescape
from datetime import datetime
from openai import OpenAI

def clean(s):
    return unescape(re.sub(r'<[^>]+>', '', s)).strip()


def fetch_tweets(api_token, username, limit=10):
    """通过 Apify API 获取 X/Twitter 账号的最新推文"""
    try:
        import httpx, time, json, os
        
        # 1. 启动抓取任务 (正确格式)
        resp = httpx.post(
            f"https://api.apify.com/v2/acts/altimis~scweet/runs",
            params={"token": api_token},
            json={
                "from_users": [username],
                "max_items": 100,  # Actor最低要求100
            },
            timeout=15
        )
        if resp.status_code != 201:
            print(f"  ⚠️ Twitter 启动失败: {resp.status_code}")
            return []
        
        run = resp.json().get("data", {})
        run_id = run.get("id")
        dataset_id = run.get("defaultDatasetId")
        if not run_id or not dataset_id:
            print(f"  ⚠️ Twitter: 无运行ID")
            return []
        
        # 2. 等待完成 (最多等 90 秒)
        for i in range(30):
            time.sleep(3)
            status = httpx.get(
                f"https://api.apify.com/v2/acts/altimis~scweet/runs/{run_id}",
                params={"token": api_token}, timeout=10
            ).json().get("data", {}).get("status", "")
            if status == "SUCCEEDED":
                break
            elif status == "FAILED":
                print(f"  ⚠️ Twitter 抓取失败")
                return []
        
        # 3. 获取结果
        items = httpx.get(
            f"https://api.apify.com/v2/datasets/{dataset_id}/items",
            params={"token": api_token}, timeout=15
        ).json()
        
        if not items:
            return []
        
        tweets = []
        for item in items:
            text = item.get("full_text") or item.get("text") or ""
            if not text:
                continue
            created = item.get("created_at", "")[:16]
            fav = item.get("favorite_count", 0)
            rt = item.get("retweet_count", 0)
            tweets.append({
                "source": "X/Twitter",
                "title": f"@{username}: {text[:80].replace(chr(10),' ')}...",
                "summary": text[:300],
                "url": f"https://x.com/{username}/status/{item.get('id','')}",
                "published": created,
                "score": min(10, 5 + fav//100 + rt//50),
                "engagement": f"❤️{fav} 🔄{rt}",
                "is_tweet": True
            })
        
        print(f"  ✅ @{username}: {len(tweets)} 条推文")
        return tweets
    except Exception as e:
        print(f"  ⚠️ Twitter 错误: {e}")
        return []


def fetch_feeds():
    """获取所有RSS源文章"""
    feeds = {
        # 🇺🇸 US Markets
        "CNBC Top News": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114",
        "Seeking Alpha": "https://seekingalpha.com/feed.xml",
        "MarketWatch": "https://feeds.marketwatch.com/marketwatch/topstories",
        
        # 🌍 Global Markets
        "Investing.com Markets": "https://www.investing.com/rss/market_overview.rss",
        "BBC Business": "https://feeds.bbci.co.uk/news/business/rss.xml",
        "The Guardian Business": "https://www.theguardian.com/business/rss",
        "The Guardian World": "https://www.theguardian.com/world/rss",
    }
    
    all_articles = []
    for name, url in feeds.items():
        try:
            f = feedparser.parse(url)
            for entry in f.entries[:15]:
                title = clean(entry.title)
                summary = clean(entry.get('summary', ''))[:300]
                link = entry.get('link', '')
                pub = entry.get('published', '')
                all_articles.append({
                    "source": name,
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "published": pub
                })
            print(f"  ✅ {name}: {min(15, len(f.entries))} 篇")
        except Exception as e:
            print(f"  ❌ {name}: {e}")
    
    return all_articles

def score_articles(articles, client):
    """让 DeepSeek 评分并分类"""
    batch_size = 30
    scored = []
    
    for i in range(0, len(articles), batch_size):
        batch = articles[i:i+batch_size]
        articles_text = "\n".join([
            f"[{j+1}] [{a['source']}] {a['title']}"
            for j, a in enumerate(batch)
        ])
        
        prompt = f"""你是一位专业的美股投资分析师。请对以下新闻进行评分(1-10分)并分类。

评分标准：
- 9-10: 重大市场事件（联储决议、重磅财报、宏观数据）
- 7-8: 重要投资主题（行业趋势、公司战略、监管变化）
- 5-6: 有价值信息（个股分析、市场观点）
- 1-4: 一般新闻（对公司投资者价值有限）

分类：market(市场), macro(宏观), earnings(财报), tech(科技), sector(板块), company(公司), policy(政策), ipo(IPO)

请为每条新闻输出格式：
[编号] 评分=X/10 | 分类=类别 | 理由=一句话

新闻列表：
{articles_text}"""

        try:
            resp = client.chat.completions.create(
                model="deepseek-v4-flash",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000,
                temperature=0.1
            )
            result = resp.choices[0].message.content
            
            for line in result.split('\n'):
                line = line.strip()
                if not line or not line.startswith('['):
                    continue
                try:
                    idx_match = re.search(r'\[(\d+)\]', line)
                    score_match = re.search(r'评分[=:](\d+(?:\.\d+)?)', line)
                    cat_match = re.search(r'分类[=:]([a-z-]+)', line)
                    
                    if idx_match and score_match:
                        idx = int(idx_match.group(1)) - 1
                        if 0 <= idx < len(batch):
                            batch[idx]['ai_score'] = float(score_match.group(1))
                            batch[idx]['category'] = cat_match.group(1) if cat_match else 'general'
                            reason = re.sub(r'\[.*?\]', '', line).strip()
                            batch[idx]['reason'] = reason[:150]
                except:
                    continue
        except Exception as e:
            print(f"  ⚠️ 评分批次 {i//batch_size + 1} 出错: {e}")
    
    # 确保所有文章都有评分
    for a in articles:
        if 'ai_score' not in a:
            a['ai_score'] = 5.0
            a['category'] = 'general'
    
    return articles

def generate_report(articles, client):
    """生成最终日报"""
    threshold = 5.0
    important = [a for a in articles if a['ai_score'] >= threshold]
    important.sort(key=lambda x: x['ai_score'], reverse=True)
    top = important[:15]
    
    # 市场数据
    print("\n=== 获取市场数据 ===")
    import urllib.request
    indices = {}
    for name, symbol in [
        # US
        ("S&P 500", "^GSPC"), ("NASDAQ", "^IXIC"), ("Dow Jones", "^DJI"),
        # Global
        ("FTSE 100", "^FTSE"), ("DAX", "^GDAXI"), ("Nikkei 225", "^N225"),
        ("Hang Seng", "^HSI"), ("Shanghai", "000001.SS"),
    ]:
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=5d&interval=1d"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(urllib.request.urlopen(req).read())
            result = data['chart']['result'][0]
            meta = result['meta']
            reg = meta.get('regularMarketPrice', 0)
            prev = meta.get('chartPreviousClose', 0)
            chg = ((reg - prev) / prev * 100) if prev else 0
            indices[name] = (reg, chg)
            print(f"  ✅ {name}: {reg:.2f} ({chg:+.2f}%)")
        except:
            indices[name] = (0, 0)
    
    # 用 DeepSeek 生成整体分析
    news_summary = "\n".join([
        f"- [{a['source']}] {a['title']} (评分:{a['ai_score']}/10)"
        for a in top[:10]
    ])
    
    market_overview = f"指数表现: S&P 500 {indices['S&P 500'][0]:.2f}({indices['S&P 500'][1]:+.2f}%), NASDAQ {indices['NASDAQ'][0]:.2f}({indices['NASDAQ'][1]:+.2f}%), Dow {indices['Dow Jones'][0]:.2f}({indices['Dow Jones'][1]:+.2f}%)"
    
    analysis_prompt = f"""你是专业的全球股票市场分析师。基于以下今日市场数据和新闻，写一段精炼的综合市场分析(中文，350字以内):

{market_overview}

重要新闻:
{news_summary}

请包含:
1. 🇺🇸 美股市场主要驱动因素
2. 🌍 全球其他市场动态 (欧洲/亚洲)
3. 📌 跨市场联动与资金流向
4. ⚡ 最值得关注的3件事
5. 📅 明日关注重点"""

    try:
        resp = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[{"role": "user", "content": analysis_prompt}],
            max_tokens=1500,
            temperature=0.3
        )
        analysis = resp.choices[0].message.content
    except:
        analysis = "AI 分析生成失败"
    
    return {
        "indices": indices,
        "articles": top,
        "all_count": len(articles),
        "analysis": analysis,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

def format_obsidian_report(data):
    """生成 Obsidian Markdown 日报"""
    indices = data['indices']
    articles = data['articles']
    
    lines = [f"""---
tags:
  - finance/us-market
  - type/daily-report
  - source/horizon
created: {datetime.now().strftime('%Y-%m-%d %H:%M')}
day: {data['date']}
week: {datetime.now().strftime('%Y-W%W')}
---

# 🇺🇸 美股日报 | US Market Daily — {data['date']}

> 📡 由 Horizon AI 雷达 + DeepSeek 自动生成

---

## 📊 今日市场概况

| 指数 | 收盘 | 涨跌 |
|------|------|------|
| **S&P 500** | {indices.get('S&P 500', (0,0))[0]:.2f} | {'**+' if indices.get('S&P 500', (0,0))[1] >= 0 else '**'}{indices.get('S&P 500', (0,0))[1]:+.2f}%** |
| **NASDAQ** | {indices.get('NASDAQ', (0,0))[0]:.2f} | {'**+' if indices.get('NASDAQ', (0,0))[1] >= 0 else '**'}{indices.get('NASDAQ', (0,0))[1]:+.2f}%** |
| **Dow Jones** | {indices.get('Dow Jones', (0,0))[0]:.2f} | {'**+' if indices.get('Dow Jones', (0,0))[1] >= 0 else '**'}{indices.get('Dow Jones', (0,0))[1]:+.2f}%** |

---

## 💡 AI 市场分析

{data['analysis']}

---

## 🔥 评分最高的新闻
"""]
    
    # 按分类分组
    from collections import defaultdict
    by_cat = defaultdict(list)
    for a in articles:
        cat = a.get('category', 'general')
        cat_names = {'market': '📊 美股', 'global': '🌍 全球', 'macro': '🌐 宏观', 'earnings': '📈 财报', 
                     'tech': '💻 科技', 'sector': '🏭 板块', 'company': '🏢 公司',
                     'policy': '⚖️ 政策', 'ipo': '🆕 IPO', 'general': '📰 其他'}
        by_cat[cat_names.get(cat, '📰 其他')].append(a)
    
    for cat_name, cat_articles in sorted(by_cat.items()):
        lines.append(f"\n### {cat_name}\n")
        for a in cat_articles:
            stars = '⭐' * max(1, min(5, round(a['ai_score'] / 2)))
            lines.append(f"- {stars} **[{a['source']}]** {a['title']}")
            lines.append(f"  - AI评分: {a['ai_score']}/10")
            if a.get('reason'):
                lines.append(f"  - {a['reason'][:120]}")
            if a.get('link'):
                lines.append(f"  - 🔗 {a['link']}")
            lines.append("")
    
    lines.append(f"""---
## 📋 数据统计

| 指标 | 数据 |
|------|------|
| 总新闻数 | {data['all_count']} 篇 |
| 通过筛选(>5分) | {len(articles)} 篇 |
| 新闻来源 | CNBC, Seeking Alpha, MarketWatch, Investing.com, BBC, Guardian |
| AI模型 | DeepSeek V4 Flash |
| 生成时间 | {datetime.now().strftime('%Y-%m-%d %H:%M')} |

---

*报告由 Horizon AI 新闻雷达 + DeepSeek 自动生成 | 所有投资决策请自行判断*
""")
    
    return '\n'.join(lines)

def main():
    api_key = os.environ.get('OPENAI_API_KEY') or os.environ.get('DASHSCOPE_API_KEY')
    if not api_key:
        # Try to read from .env
        try:
            with open(os.path.expanduser('~/Workspace/horizon-news/.env')) as f:
                for line in f:
                    if 'OPENAI_API_KEY=' in line:
                        api_key = line.strip().split('=', 1)[1]
                        break
        except:
            pass
    
    if not api_key:
        print("❌ 未设置 API Key")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")
    
    print("🌅 美股日报生成器")
    print("=" * 50)
    
    print("\n📡 获取新闻...")
    articles = fetch_feeds()
    
    # 同时获取 Twitter/X 内容
    print("\n🐦 获取 X/Twitter...")
    apify_token = os.environ.get('APIFY_TOKEN') or ''
    if apify_token and not apify_token.endswith('xxx'):
        tweets = fetch_tweets(apify_token, 'aleabitoreddit', limit=8)
        for t in tweets:
            articles.append(t)
        print(f"   合计: {len(articles)} 条内容 (含 Twitter)")
    print(f"\n📥 共获取 {len(articles)} 条新闻")
    
    print("\n🤖 DeepSeek 评分中...")
    articles = score_articles(articles, client)
    scored = [a for a in articles if a.get('ai_score', 0) > 0]
    print(f"\n⭐ 已评分: {len(scored)} 条")
    
    print("\n📝 生成日报...")
    report_data = generate_report(articles, client)
    
    print("\n💾 保存日报...")
    import sys
    date_str = report_data['date']
    filename = f"US Market Daily {date_str}.md"
    
    # 同时保存到 data/summaries/ (用于 GitHub Pages)
    summaries_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'summaries')
    os.makedirs(summaries_dir, exist_ok=True)
    filepath = os.path.join(summaries_dir, filename)
    
    # 如果是 macOS, 也保存到 Obsidian
    if sys.platform == 'darwin':
        obsidian_path = os.path.expanduser(
            "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/又又的obsidian news/Stocks News"
            "/30.areas/finance/US Market Daily"
        )
        os.makedirs(obsidian_path, exist_ok=True)
        obsidian_file = os.path.join(obsidian_path, filename)
        with open(obsidian_file, 'w') as f:
            f.write(report)
        print(f"  📁 也保存到 Obsidian")
    
    report = format_obsidian_report(report_data)
    with open(filepath, 'w') as f:
        f.write(report)
    
    print(f"\n✅ 日报已生成!")
    print(f"📁 位置: {filepath}")
    print(f"📊 新闻: {report_data['all_count']} 篇→筛选{len(report_data['articles'])}篇")
    print(f"📈 三大指数全覆盖")

if __name__ == '__main__':
    main()
