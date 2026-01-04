#!/bin/bash

# Check arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: ./gen_problem.sh <Problem_Number> \"<Problem_Name>\""
    exit 1
fi

PROB_NUM=$1
PROB_NAME=$2

# Calculate directory hierarchy (e.g., 217 -> 0201-0300)
START=$(( ( (PROB_NUM - 1) / 100 ) * 100 + 1 ))
END=$(( START + 99 ))
RANGE_DIR=$(printf "%04d-%04d" $START $END)
PROB_DIR=$(printf "%04d. %s" $PROB_NUM "$PROB_NAME")

TARGET_PATH="$RANGE_DIR/$PROB_DIR"

# Create directories
mkdir -p "$TARGET_PATH"/{cpp,python,java,c}

# Create empty files
touch "$TARGET_PATH/Description.md"
touch "$TARGET_PATH/python/Solution.py"
touch "$TARGET_PATH/cpp/Solution.cpp"
touch "$TARGET_PATH/java/Solution.java"
touch "$TARGET_PATH/c/Solution.c"

echo "Successfully created boilerplate for: $PROB_DIR"