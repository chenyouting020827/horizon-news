---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 106 items, 12 important content pieces were selected

---

1. [Anthropic Publicly Releases Claude Models' System Prompts](#item-1) ⭐️ 9.0/10
2. [Third-World Embedded Engineer Challenges RISC-V Cost Assumptions](#item-2) ⭐️ 8.0/10
3. [NIH Ends Key Grant for Budding Clinical Researchers](#item-3) ⭐️ 8.0/10
4. [U.S. Tells Allies to Pick Sides in AI Race with China](#item-4) ⭐️ 8.0/10
5. [AI API Credit Resale: The Gray Market for Unused Tokens](#item-5) ⭐️ 7.0/10
6. [Firefox for iOS Adds Native Adblocker](#item-6) ⭐️ 7.0/10
7. [Three Control Rods Drop into St. Lucie Reactor Core; Unit 1 Manually Shut Down](#item-7) ⭐️ 6.0/10
8. [Hobbyist Hosts a Real Telnet BBS on a Casio Calculator](#item-8) ⭐️ 6.0/10
9. [Weekend at 100: Modern Work Habits Are Reshaping Our Rest](#item-9) ⭐️ 6.0/10
10. [Public AI with Shared Memory Across All Users Is Live on HN](#item-10) ⭐️ 6.0/10
11. [Nvidia reportedly weighs $3B investment in SB Energy for OpenAI data center](#item-11) ⭐️ 6.0/10
12. [Deepfake Albanese scams cost Australians $7.4m, ASIC warns](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Publicly Releases Claude Models' System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 9.0/10

Anthropic has publicly released the system prompts that govern its Claude models, with instructions now visible for versions including Opus 5 and Fable 5. This is a rare transparency step: such prompts are usually kept hidden and have rarely been published so openly before. Researchers, auditors, and developers can now inspect exactly how Anthropic steers Claude's behavior, from crisis-response rules to image-handling checks. This enables version-to-version analysis of safety mechanisms and opens a new channel for accountability and empirical study of frontier models. The published prompts contain nuanced behavioral rules—e.g., prioritizing user wellbeing over task completion when someone is in crisis, and explicitly checking whether an uploaded image actually exists before assuming one is present. Simon Willison mirrored the documents as a git history to expose cross-version changes.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Background**: System prompts are the hidden instructions that set a model's context, tone, and safety constraints before each user turn. Anthropic shapes Claude not only through these prompts but also through constitutional training and a layered alignment system. Claude models come in tiers like Haiku, Sonnet, and Opus; recent releases such as Fable 5 and Mythos 5 have been added to the lineup.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://promptengineering.org/system-prompts-in-large-language-models/">System Prompts in Large Language Models</a></li>

</ul>
</details>

**Discussion**: Reactions were largely positive but not uncritical. Simon Willison contributed a git history of the prompts, calling attention to additions like 'Claude Fable 5' and the rule to verify image uploads. Others questioned the image-check prompt, arguing that even powerful models like Opus 4.8 still need reminders for basic common sense, and one commenter accused the forum of suppressing AI-critical stories.

**Tags**: `#AI`, `#LLM`, `#transparency`, `#Claude`, `#system prompts`

---

<a id="item-2"></a>
## [Third-World Embedded Engineer Challenges RISC-V Cost Assumptions](https://rvembedded.com/blog_post/12/) ⭐️ 8.0/10

A blog post by an embedded engineer from a developing country responds to the article "RISC-V They Should Have Known Better," arguing that low-cost hardware and educational access matter differently outside the Bay Area. The post highlights how shipping costs and hardware availability shape learning opportunities in countries like Nigeria and Bangladesh. This perspective counters the usual Bay Area-centric RISC-V discussion, showing that open-hardware initiatives can reduce barriers to embedded engineering education globally. It underscores that real-world logistics and costs, not just technical specifications, drive adoption in developing countries. The post is published on rvembedded.com, which also hosts a Project Lab for students. One commenter disputes the $60 shipping cost claim for Nigeria and Bangladesh, noting that these countries sit on major global trade routes with inexpensive last-mile delivery.

hackernews · Narishma · Aug 16, 17:01 · [Discussion](https://news.ycombinator.com/item?id=49321717)

**Background**: RISC-V is an open-standard instruction set architecture (ISA) that defines how RISC-V processors are designed and is free to use without licensing fees. This openness makes it attractive for education and low-cost hardware, especially where proprietary chip costs are prohibitive. Embedded engineers use RISC-V to build microcontrollers and other systems, and educational initiatives like rvembedded.com aim to teach these skills in underserved regions.

<details><summary>References</summary>
<ul>
<li><a href="https://riscv.org/specifications/ratified/">Ratified Specifications - RISC - V International</a></li>

</ul>
</details>

**Discussion**: Comments are generally positive, praising the article as a breath of fresh air compared to usual Bay Area takes. One user disputes the shipping cost claim for Nigeria and Bangladesh, while another celebrates the rvembedded.com initiative and Project Lab. Overall, readers are appreciative and offer constructive technical disagreement.

**Tags**: `#RISC-V`, `#embedded systems`, `#global development`, `#hardware`, `#education`

---

<a id="item-3"></a>
## [NIH Ends Key Grant for Budding Clinical Researchers](https://www.science.org/content/article/nih-ending-key-grant-budding-clinical-researchers) ⭐️ 8.0/10

The U.S. National Institutes of Health is discontinuing a key institutional training grant that supports early-career clinical researchers, a move that has alarmed the biomedical research community. This decision threatens the pipeline of physician-scientists and clinical researchers, who rely on such grants for protected time, salary support, and mentored research training. It could accelerate talent loss and weaken the nation's biomedical research capacity. The affected grants include K12 and KL2 career development awards, which are institutional two-year programs providing salary and research support for junior faculty. The NIH has not provided a clear public rationale, and the phase-out appears tied to broader budget cuts and administrative restructuring.

hackernews · brandonb · Aug 16, 16:14 · [Discussion](https://news.ycombinator.com/item?id=49321353)

**Background**: NIH offers a range of career development 'K awards' to help researchers transition from postdoctoral training to independent faculty positions. K12 and KL2 are institutional awards that let universities and medical centers train cohorts of junior clinical researchers, often across specific fields such as women's health, cancer, or translational science. These programs are seen as critical gateways for clinicians who want to pursue research careers alongside patient care.

<details><summary>References</summary>
<ul>
<li><a href="https://researchtraining.nih.gov/">Research Training and Career Development | Grants & Funding</a></li>
<li><a href="https://ncats.nih.gov/research/research-activities/ctsa/applicant-information/research-training-career-development-awards">Application Information for CTSA Program Research Training ...</a></li>
<li><a href="https://georgiactsa.org/training/kl2.html">Georgia CTSA KL2 Scholars Program: Career Development for ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely condemn the decision, with some arguing it reflects deliberate efforts to weaken U.S. science, while others attribute it to severe NIH mismanagement. Several lament a generational loss of young talent, noting postdocs in cancer, Alzheimer's, and Parkinson's research are leaving the country or abandoning the field. One comment contains inflammatory political language.

**Tags**: `#science policy`, `#NIH`, `#research funding`, `#clinical research`, `#academia`

---

<a id="item-4"></a>
## [U.S. Tells Allies to Pick Sides in AI Race with China](https://www.cnbc.com/2026/08/15/us-to-tell-allies-they-must-pick-sides-in-ai-race-with-china-reuters.html) ⭐️ 8.0/10

Reuters reports that the U.S. is sending a draft letter to the 35 signatories of its AI Opportunity Statement, urging them to pick sides in the AI race with China. The letter follows the statement signed in June at the Pax Silica Summit. This signals a significant escalation in U.S.-China tech rivalry, forcing allied nations to make a diplomatic choice that could reshape global AI supply chains and collaboration. It affects technology companies and governments worldwide, potentially splitting the global AI ecosystem into competing blocs. The draft letter is addressed to the 35 countries that signed the U.S.-led AI Opportunity Statement in June 2026. Reuters says the letter asks signatories to clearly commit to U.S. positions on AI governance, trusted supply chains, and industrial capacity.

rss · CNBC Top News · Aug 15, 22:49

**Background**: The AI Opportunity Statement was adopted at the Pax Silica Summit in June, where 35 nations committed to pro-growth AI collaboration with the U.S. It focuses on AI governance, trusted supply chains, and industrial capacity, serving as a diplomatic tool to counter China's AI influence. The new draft letter appears to turn that statement into a demand for political alignment, asking countries to formally choose a side in the U.S.-China AI rivalry.

<details><summary>References</summary>
<ul>
<li><a href="https://www.state.gov/ai-opportunity-statement">AI Opportunity Statement - United States Department of State</a></li>
<li><a href="https://currentaffairs.adda247.com/35-nations-sign-ai-opportunity-statement-at-pax-silica-summit/">35 Nations Sign AI Opportunity Statement at Pax Silica Summit</a></li>
<li><a href="https://edunovations.com/currentaffairs/international/ai-opportunity-statement-at-pax-silica-summit-2026/">AI Opportunity Statement At Pax Silica Summit 2026: 35 Nations...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#US-China`, `#Geopolitics`, `#Technology regulation`

---

<a id="item-5"></a>
## [AI API Credit Resale: The Gray Market for Unused Tokens](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

A new Vectoral blog post titled Who Are the Token Brokers? examines an emerging resale economy where brokers trade unused AI API credits at a discount. This informal market, often involving credits from startup accelerators and free tiers, raises trust, security, and policy concerns. The gray market undermines official AI pricing, enables model distillation by third parties, and creates new fraud surfaces such as hacked accounts. It affects AI platforms like OpenAI and Anthropic, as well as legitimate developers who compete with cut-rate resellers. Reseller access can cost roughly 7–30% of official list prices, and sources range from educational grants (e.g., YC Startup School credits) to stolen cards and mass-created free-tier accounts. Because brokers often route traffic through proxies, TLS end-to-end integrity is lost, allowing traffic manipulation and secret exfiltration.

hackernews · mlenhard · Aug 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49320611)

**Background**: AI API credits are prepaid usage allowances for services like OpenAI's API, often awarded through promotions or startup programs. A gray market for these credits has developed, with brokers selling access at steep discounts and using techniques like VPN/IP masking to obscure origins. This market is linked to AI distillation, where models are trained on outputs from other models, and to long-standing abuse patterns similar to loyalty-account fraud.

<details><summary>References</summary>
<ul>
<li><a href="https://www.blackhatworld.com/seo/how-does-the-gray-market-for-cheaper-llm-api-tokens-work.1826427/">How does the gray market for cheaper LLM API tokens work? | BlackHatWorld</a></li>
<li><a href="https://explainx.ai/blog/ai-token-black-market-claude-resellers-distillation-2026">AI Token Black Market: Claude Resellers at 70–93% Off (2026) | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-ai-distillation-gray-market-access-western-models">What Is AI Distillation? How Chinese Labs Use Gray Market Access to Train on Western Models | MindStudio</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical, arguing that trusting a third-party broker invites account hacking and private data leaks. Several noted that providers can easily detect and ban relay IP addresses, while others highlighted distillation and mass account creation as recurring abuse patterns. The discussion also flagged serious security risks from proxy-mediated traffic, including tool-call manipulation and secret exfiltration.

**Tags**: `#AI`, `#credits`, `#gray market`, `#economics`, `#API`

---

<a id="item-6"></a>
## [Firefox for iOS Adds Native Adblocker](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 7.0/10

Firefox for iOS now includes a native adblocker built directly into the browser, allowing users to block ads without installing third-party extensions. The feature is available through Mozilla's support documentation as of this update. This simplifies ad blocking on iOS, where extension support is extremely limited, and improves privacy and page-load performance for Firefox users. It also brings Firefox on par with other iOS browsers that already offer built-in content blocking. According to Mozilla's support page, the adblocker blocks ads on search engine results pages including Google, Bing, DuckDuckGo, and other providers. Because Firefox for iOS uses WebKit, content blocking is implemented through Apple's content blocker API, which may be less flexible than desktop extensions such as uBlock Origin.

hackernews · pentagrama · Aug 16, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49319633)

**Background**: iOS requires all browsers to use the WebKit engine, so Firefox for iOS cannot use Mozilla's own Gecko engine or support traditional browser extensions. To block content, developers must use Apple's content blocker API, which applies a predefined set of rules rather than running arbitrary code. As a result, a native adblocker removes the need for Firefox iOS users to download separate content-blocking apps or switch to Firefox Focus. This update reflects the constraints of the iOS ecosystem while simplifying ad blocking for everyday users.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Safari_content_blockers">Safari content blockers</a></li>
<li><a href="https://webkit.org/blog/3476/content-blockers-first-look/">Introduction to WebKit Content Blockers</a></li>
<li><a href="https://developer.apple.com/documentation/webkit/wkcontentrulelist">WKContentRuleList | Apple Developer Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Firefox Focus already had a system-wide adblocker through iOS content blockers, and several praised uBlock Origin Lite for Safari as a strong alternative. Some users expressed frustration about the lack of extension support on iOS, with one mentioning Orion as a browser that supports extensions. Overall, the discussion viewed the move positively but highlighted existing options and iOS limitations.

**Tags**: `#firefox`, `#ios`, `#adblocking`, `#privacy`, `#browser`

---

<a id="item-7"></a>
## [Three Control Rods Drop into St. Lucie Reactor Core; Unit 1 Manually Shut Down](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) ⭐️ 6.0/10

Unit 1 at the St. Lucie nuclear power plant in Florida was manually shut down after three control rods unexpectedly dropped into the reactor core. Operators initiated the shutdown to restore the reactor to a safe, subcritical state. The incident demonstrates the defense-in-depth design of U.S. pressurized water reactors, where dropped rods absorb neutrons to reduce reactivity even during an unplanned event. It matters because it can reassure the public about reactor safety while highlighting how equipment glitches or procedural issues can trigger shutdowns. The three rods are neutron-absorbing control elements used to regulate or terminate the chain reaction; their unplanned drop required the manual shutdown to bring the core to a subcritical state. This is not the first such event at the plant: one commenter notes an almost identical 2024 occurrence, with a root cause reportedly involving a procedural issue and electrical failure.

hackernews · toomuchtodo · Aug 16, 15:16 · [Discussion](https://news.ycombinator.com/item?id=49320856)

**Background**: Control rods contain neutron-absorbing material and are the primary mechanism for regulating the fission rate in a nuclear reactor. In an emergency, a scram inserts all control rods into the core to rapidly terminate the chain reaction. Because a dropped rod removes neutrons from the reaction, reactor designs anticipate occasional rod drops and respond by shutting down or rebalancing reactivity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scram">Scram - Wikipedia</a></li>
<li><a href="https://explorenuclear.com/control-rods/">Control Rods – How to control a nuclear reactor | Explore Nuclear</a></li>

</ul>
</details>

**Discussion**: The comments are largely level-headed: several explain that a dropped rod is a designed-for condition and that a single fully inserted rod can make a U.S. PWR subcritical. One commenter has mixed feelings—nothing serious happened and all systems worked, yet the root cause of the rod drop still needs explaining. Another points out a similar event at the same plant in 2024 and links to the NRC entry.

**Tags**: `#nuclear`, `#safety`, `#reactor`, `#control rods`, `#incident`

---

<a id="item-8"></a>
## [Hobbyist Hosts a Real Telnet BBS on a Casio Calculator](https://ei3lh.eu/2026/08/16/a-true-telnet-bbs-on-a-casio-calculator/) ⭐️ 6.0/10

An author has built and is running a genuine Telnet BBS entirely on a Casio VX-4 calculator with only 8KB of RAM, connecting it to the Internet for remote callers. The project shows how a calculator's BASIC environment can be pushed to serve a real interactive bulletin board. This is a charming example of retrocomputing combined with modern networking, proving that severely constrained hardware can still host classic online services. It will appeal to hobbyists interested in creative hardware hacks, minimal programming, and the history of online communities. The project is built on Casio BASIC and runs on a Casio VX-4 with just 8KB of RAM, which imposes severe limits on code size and message storage. The author plans to explore ways to publish the BBS safely while still making it clear to visitors that they are connecting to a real Telnet BBS hosted on a calculator.

hackernews · austinallegro · Aug 16, 12:16 · [Discussion](https://news.ycombinator.com/item?id=49319349)

**Background**: Bulletin Board Systems (BBSes) were early online communities, originally accessed via dial-up modems; later, Telnet allowed Internet users to connect to them. Casio BASIC is a programming language found on many Casio calculators, enabling simple software but normally not network services. Running a Telnet server on an 8KB-RAM calculator requires extremely tight coding, making the feat a notable retrocomputing stunt.

<details><summary>References</summary>
<ul>
<li><a href="https://ei3lh.eu/2026/08/16/a-true-telnet-bbs-on-a-casio-calculator/">A True Telnet BBS On A Casio Calculator . – EI3LH</a></li>
<li><a href="https://en.wikipedia.org/wiki/Casio_BASIC">Casio BASIC - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were mostly positive and nostalgic, with one praising the journal-style writing and another noting that the quirky font and colors made the output hard to read. Others shared personal memories of Casio calculators and related hobby purchases, while one commenter specifically enjoyed the AI-generated fake magazine advert for the VX-4.

**Tags**: `#retrocomputing`, `#telnet`, `#bbs`, `#casio`, `#hobbyist`

---

<a id="item-9"></a>
## [Weekend at 100: Modern Work Habits Are Reshaping Our Rest](https://www.theguardian.com/money/2026/aug/16/the-weekend-is-100-years-old-skiveday-fridays-and-hybrid-working-ruined-it) ⭐️ 6.0/10

An article marks the 100th anniversary of the weekend, tracing its origins and arguing that modern trends such as 'skiveday Fridays' and hybrid working have eroded it. It has prompted reader debate about whether the weekend is a natural rhythm or a social construct. The discussion matters because it questions a fundamental pillar of modern work-life balance: the weekend. How societies reshape time off will affect labor policy, family life, and mental health for millions of workers. The article frames the weekend not as an eternal institution but as a roughly 100-year-old social construction tied to the industrial clock. Readers debate alternatives such as a four-day workweek and question whether the current structure suits family or community life.

hackernews · lentil_soup · Aug 16, 15:30 · [Discussion](https://news.ycombinator.com/item?id=49320984)

**Background**: The seven-day week has no astronomical basis; historians treat it as a social and cultural institution, and the modern two-day weekend emerged with industrialization and labor reforms. As remote and hybrid work blur the boundaries between work and home, the traditional Saturday-Sunday container is being challenged by proposals for shorter or more flexible schedules.

**Discussion**: Commenters highlight that even the week itself is a recent social construct, not a natural unit. Some propose symbolic moves like making every Friday a labor day, others cautiously support the four-day workweek, and one reader questions whether phrases about 'reclaiming autonomy' overstate what rest days can truly deliver.

**Tags**: `#history`, `#work-life-balance`, `#culture`, `#labor`, `#weekend`

---

<a id="item-10"></a>
## [Public AI with Shared Memory Across All Users Is Live on HN](https://wildstatic.com/) ⭐️ 6.0/10

A developer posted 'Show HN' for wildstatic.com, a public AI whose memory is shared across all users rather than siloed per person. It aims to learn collectively, but already shows repetition fatigue and starts selectively ignoring messages under heavy load. Shared-memory AI could accelerate collective learning and reduce redundant prompts in teams, but it also introduces new abuse and governance risks. The project revives debates about public AI safety that date back to Microsoft's Tay incident. Because the memory is global, the AI can grow tired of repeating answers to new visitors, and under front-page traffic it began selectively ignoring messages. The developer said they were 'tweaking some stuff' in response to the unexpected attention.

hackernews · adjohu · Aug 16, 13:21 · [Discussion](https://news.ycombinator.com/item?id=49319814)

**Background**: Conventional chatbots typically keep isolated memory per user, so shared-memory systems are an experimental direction for collective intelligence. Products such as Mem0 and claude-mem show growing interest in persistent AI memory. However, public shared context can be gamed, and fatigue or repetition can emerge when many users query the same model. As one analysis notes, AI memory is about meaning, not just storing every exchange.

<details><summary>References</summary>
<ul>
<li><a href="https://mem0.ai/">Mem0 - AI Memory Layer for your Agents & Apps | Persistent Context</a></li>
<li><a href="https://cmem.ai/">claude-mem + cmem — AI agent memory , everywhere</a></li>
<li><a href="https://medium.com/@wojciech.gorecki/remember-i-havent-forgotten-on-the-need-for-true-memory-in-ai-systems-483132c78a82">Remember, I haven’t forgotten. On the Need for True Memory in AI ...</a></li>

</ul>
</details>

**Discussion**: Commenters were cautiously optimistic: one developer said a shared session improved their team's output quality, another had tried a similar idea that flopped. Others warned that 'folks forgot the lessons of tay.ai,' and the developer acknowledged repetition fatigue under front-page load.

**Tags**: `#AI`, `#shared memory`, `#chatbot`, `#collective intelligence`, `#Show HN`

---

<a id="item-11"></a>
## [Nvidia reportedly weighs $3B investment in SB Energy for OpenAI data center](https://www.cnbc.com/2026/08/15/nvidia-mulls-3b-investment-in-sb-energy-in-openai-data-center-deal-report.html) ⭐️ 6.0/10

Nvidia is reportedly in talks to invest $3 billion in SoftBank's SB Energy as part of a plan to provide credit support for an OpenAI data center campus in Ohio, according to The Information. This deal illustrates how the AI boom is driving investment beyond chips into energy and data-center financing, and it could deepen Nvidia's strategic ties with OpenAI and SoftBank. The investment is intended as credit support for a planned Ohio data center campus, and the deal is still under discussion. SB Energy, backed by SoftBank and OpenAI, earlier this year secured a $1 billion investment and a 1.2 GW lease from OpenAI for AI data centers.

rss · CNBC Top News · Aug 15, 20:32

**Background**: Large-scale AI data center projects require massive capital and credit support from multiple parties. SB Energy is a SoftBank-and-OpenAI-backed company that develops energy and data center infrastructure. In March 2026, OpenAI committed $1 billion and a 1.2 GW lease to SB Energy, reflecting a broader trend of integrating energy supply with AI computing. Nvidia's potential $3 billion investment would add a major chipmaker to this financing structure.

<details><summary>References</summary>
<ul>
<li><a href="https://sbenergy.com/openai-and-softbank-group-partner-with-sb-energy/">OpenAI and SoftBank Group Partner with SB Energy</a></li>
<li><a href="https://sbenergy.com/">SB Energy</a></li>
<li><a href="https://www.moodys.com/web/en/us/insights/credit-risk/data-centers.html">Credit Risk Insights for Global Data Centers - Moody's</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#OpenAI`, `#Data Center`, `#Investment`, `#Energy`

---

<a id="item-12"></a>
## [Deepfake Albanese scams cost Australians $7.4m, ASIC warns](https://www.theguardian.com/australia-news/2026/aug/17/deepfake-anthony-albanese-used-in-celebrity-scams-duping-australians-out-of-74m-asic-warns) ⭐️ 6.0/10

Australia's corporate watchdog, ASIC, issued a warning about a steep rise in deepfakes of celebrities and politicians used to lure victims into phony investment opportunities. Anthony Albanese is the figure most commonly co-opted, and these scams have defrauded Australians of $7.4 million. This highlights the tangible financial harm caused by deepfake technology, underscoring the urgent need for stronger AI safety measures and public awareness. It affects Australian consumers directly and raises concerns about the misuse of political figures' likenesses in fraud. The scams use deepfakes to promote phony investment opportunities, with Prime Minister Anthony Albanese being the most commonly used likeness. ASIC's warning comes amid a broader rise in AI-generated fraud targeting Australians.

rss · The Guardian World · Aug 16, 14:01

**Background**: Deepfakes are synthetic media created using artificial intelligence, often making people appear to say or do things they never did. Scammers increasingly use them to fabricate celebrity or political endorsements for investment fraud. This case reflects a global trend where deepfake technology is weaponized for financial scams, prompting regulators to respond.

**Tags**: `#deepfakes`, `#AI safety`, `#scams`, `#cybersecurity`, `#Australia`

---