#!/bin/bash

# --- Language Mapping Table ---
declare -A LANG_MAP
LANG_MAP=(
    ["cpp"]="cpp:cpp" ["java"]="java:java" ["python"]="python:py"
    ["python3"]="python:py" ["py"]="python:py" ["javascript"]="javascript:js"
    ["typescript"]="typescript:ts" ["csharp"]="csharp:cs" ["c"]="c:c"
    ["go"]="go:go" ["rust"]="rust:rs" ["rs"]="rust:rs"
)

CHOSEN_LANGS=()
INPUT_STR=""

show_help() {
    echo -e "Usage: ./gen_problem.sh [Options] <Problem Name | ID>"
    echo -e "\nOptions:"
    echo -e "  -h          Show help."
    echo -e "  -all        Templates for py, cpp, java, c, rs, go."
    echo -e "  -l <langs>  Custom languages (space separated)."
    exit 0
}

# --- Parsing Logic: Smart Identification ---
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h) show_help ;;
        -all) CHOSEN_LANGS=("python3" "cpp" "java" "c" "rust" "go"); shift ;;
        -l)
            shift
            while [[ "$#" -gt 0 && ! "$1" =~ ^- ]]; do
                # Only add if it's a known key in LANG_MAP
                if [[ -n "${LANG_MAP[${1,,}]}" ]]; then
                    CHOSEN_LANGS+=("${1,,}")
                    shift
                else
                    # Might be the Problem ID, exit inner loop
                    break
                fi
            done
            ;;
        *)
            # Accumulate everything else as the problem name/ID
            if [[ -z "$INPUT_STR" ]]; then
                INPUT_STR="$1"
            else
                INPUT_STR="$INPUT_STR $1"
            fi
            shift
            ;;
    esac
done

# Defaults to python3 if no language is specified
if [ ${#CHOSEN_LANGS[@]} -eq 0 ]; then CHOSEN_LANGS=("python3"); fi
if [[ -z "$INPUT_STR" ]]; then show_help; fi

# --- Fetch Metadata (The rest of the logic remains the same) ---
echo "🚀 Fetching metadata for: $INPUT_STR..."
METADATA=$(python3 -c "
import requests, re, sys
input_data = '$INPUT_STR'.strip()
is_id = re.match(r'^\d+$', input_data)
url = 'https://leetcode.com/graphql'
if is_id:
    r = requests.post(url, json={'query': 'query { allQuestions { questionId titleSlug title } }'})
    target = next((q for q in r.json()['data']['allQuestions'] if q['questionId'] == input_data), None)
else:
    slug = input_data.lower().replace(' ', '-')
    r = requests.post(url, json={'query': 'query(\$slug: String!) { question(titleSlug: \$slug) { questionId title titleSlug } }', 'variables': {'slug': slug}})
    target = r.json()['data']['question']
if target: print(f\"{target['questionId']}|{target['title']}|{target['titleSlug']}\")
" 2>/dev/null)

if [ -z "$METADATA" ]; then
    echo "❌ [Access Denied]: Could not identify problem '$INPUT_STR'."
    exit 1
fi

PROB_NUM=$(echo "$METADATA" | cut -d'|' -f1)
PROB_NAME=$(echo "$METADATA" | cut -d'|' -f2)
PROB_SLUG=$(echo "$METADATA" | cut -d'|' -f3)

START=$(( ( (PROB_NUM - 1) / 100 ) * 100 + 1 ))
END=$(( START + 99 ))
RANGE_DIR=$(printf "%04d-%04d" $START $END)
PROB_DIR=$(printf "%04d. %s" $PROB_NUM "$PROB_NAME")
TARGET_PATH="$RANGE_DIR/$PROB_DIR"

# Create Directory & Description
mkdir -p "$TARGET_PATH"
if [ ! -f "$TARGET_PATH/Description.md" ]; then
    python3 fetch_problem.py "$PROB_SLUG" --markdown > "$TARGET_PATH/Description.md" 2>/dev/null
    echo "📝 [Created]: Description.md"
else
    echo "ℹ️ [Established]: Description.md"
fi

# Injection Loop
for L in "${CHOSEN_LANGS[@]}"; do
    case $L in
        py|python|python3) L_SLUG="python3" ;;
        rs|rust) L_SLUG="rust" ;;
        *) L_SLUG=$L ;;
    esac

    MAP_VAL=${LANG_MAP[$L_SLUG]}
    if [ -z "$MAP_VAL" ]; then continue; fi

    SUBDIR=$(echo "$MAP_VAL" | cut -d':' -f1)
    EXT=$(echo "$MAP_VAL" | cut -d':' -f2)
    FILE_PATH="$TARGET_PATH/$SUBDIR/Solution.$EXT"

    if [ -f "$FILE_PATH" ]; then
        echo "⚠️ [Established]: $SUBDIR solution exists."
    else
        mkdir -p "$TARGET_PATH/$SUBDIR"
        python3 fetch_problem.py "$PROB_SLUG" --code "$L_SLUG" > "$FILE_PATH"
        echo "✅ [Injected]: $SUBDIR template created."
    fi
done

echo -e "\n🎯 [Service Restored]: Setup complete for $PROB_NAME."