#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: ./gen_problem.sh <Num> \"<Name>\""
    exit 1
fi

PROB_NUM=$1
PROB_NAME=$2

# 自動轉換 Slug: "Two Sum" -> "two-sum"
PROB_SLUG=$(echo "$PROB_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

START=$(( ( (PROB_NUM - 1) / 100 ) * 100 + 1 ))
END=$(( START + 99 ))
RANGE_DIR=$(printf "%04d-%04d" $START $END)
PROB_DIR=$(printf "%04d. %s" $PROB_NUM "$PROB_NAME")
TARGET_PATH="$RANGE_DIR/$PROB_DIR"

mkdir -p "$TARGET_PATH"/{cpp,python,java,c}

# 調用 Python 抓取並生成漂亮 Markdown
echo "🚀 Fetching high-quality description for: $PROB_NAME..."
python3 fetch_problem.py "$PROB_SLUG" > "$TARGET_PATH/Description.md"

# 建立空檔案
touch "$TARGET_PATH/python/Solution.py"
touch "$TARGET_PATH/cpp/Solution.cpp"
touch "$TARGET_PATH/java/Solution.java"
touch "$TARGET_PATH/c/Solution.c"

echo "✅ Done! Path: $TARGET_PATH"