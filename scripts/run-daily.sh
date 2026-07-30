#!/bin/bash
# 一键生成美股日报
set -e

HORIZON_DIR="$HOME/Workspace/horizon-news"
cd "$HORIZON_DIR"

# 加载 API key
export OPENAI_API_KEY=$(grep -E '^OPENAI_API_KEY=' .env | head -1 | cut -d= -f2)
export PYTHONUNBUFFERED=1

echo "🌅 美股日报生成器 v1.0"
echo "======================="
date

uv run python3 -u scripts/daily_report.py
