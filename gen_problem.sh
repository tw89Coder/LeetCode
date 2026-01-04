#!/bin/bash

# 檢查輸入參數
if [ "$#" -ne 2 ]; then
    echo "Usage: ./gen_problem.sh <Problem_ID> <Problem_Name>"
    echo "Example: ./gen_problem.sh 1 \"Two Sum\""
    exit 1
fi

ID=$1
NAME=$2

# 計算分層範圍 (例如 1 變為 0001-0100)
START=$(( ( (ID - 1) / 100 ) * 100 + 1 ))
END=$(( START + 99 ))
RANGE=$(printf "%04d-%04d" $START $END)

# 格式化問題資料夾名稱 (例如 0001. Two Sum)
DIR_NAME=$(printf "%04d. %s" $ID "$NAME")

# 建立路徑
TARGET_PATH="$RANGE/$DIR_NAME"
mkdir -p "$TARGET_PATH/cpp" "$TARGET_PATH/python"

# 建立基礎檔案
touch "$TARGET_PATH/Description.md"

echo "✅ Created: $TARGET_PATH"