#!/bin/bash

# --- Path Resolution Logic ---
# SCRIPT_DIR: The absolute path of the directory where this script resides.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# REPO_ROOT: Dynamically determines the project root. 
# If the script is inside a 'scripts' folder, it moves up one level.
if [[ "$(basename "$SCRIPT_DIR")" == "scripts" ]]; then
    REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
else
    REPO_ROOT="$SCRIPT_DIR"
fi

# Switch to root to ensure directory structures start from the top level.
cd "$REPO_ROOT"

# --- Language Mapping Table ---
# Maps user-friendly aliases to LeetCode's langSlugs and file extensions.
declare -A LANG_MAP
LANG_MAP=(
    ["cpp"]="cpp:cpp" ["java"]="java:java" ["python"]="python:py"
    ["python3"]="python:py" ["py"]="python:py" ["javascript"]="javascript:js"
    ["typescript"]="typescript:ts" ["csharp"]="csharp:cs" ["c"]="c:c"
    ["go"]="go:go" ["rust"]="rust:rs" ["rs"]="rust:rs" ["swift"]="swift:swift"
    ["kotlin"]="kotlin:kt" ["ruby"]="ruby:rb" ["php"]="php:php"
)

CHOSEN_LANGS=()
INPUT_STR=""

# --- Help Menu ---
show_help() {
    echo -e "Usage: $0 [Options] <Problem Name | ID>"
    echo -e "\nOptions:"
    echo -e "  -h          Display this help protocol and exit."
    echo -e "  -all        Generate templates for major languages (py, cpp, java, c, rs, go)."
    echo -e "  -l <langs>  Specify custom languages (space separated, e.g., -l py rust)."
    echo -e "\nExamples:"
    echo -e "  $0 242 -l py cpp"
    echo -e "  $0 Valid Anagram -all"
    exit 0
}

# --- Argument Parsing: Smart Identification ---
# This loop distinguishes between flags, language aliases, and problem identifiers.
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h) show_help ;;
        -all) CHOSEN_LANGS=("python3" "cpp" "java" "c" "rust" "go"); shift ;;
        -l)
            shift
            while [[ "$#" -gt 0 && ! "$1" =~ ^- ]]; do
                # Check if the input exists in our protocol mapping.
                if [[ -n "${LANG_MAP[${1,,}]}" ]]; then
                    CHOSEN_LANGS+=("${1,,}")
                    shift
                else
                    # Break if the token is likely the Problem ID/Name.
                    break
                fi
            done
            ;;
        *)
            # Accumulate remaining tokens as the problem identifier.
            if [[ -z "$INPUT_STR" ]]; then INPUT_STR="$1"; else INPUT_STR="$INPUT_STR $1"; fi
            shift
            ;;
    esac
done

# Default to Python3 if the user is 'lazy' and provides no language flags.
if [ ${#CHOSEN_LANGS[@]} -eq 0 ]; then CHOSEN_LANGS=("python3"); fi
if [[ -z "$INPUT_STR" ]]; then show_help; fi

# --- Metadata Retrieval (GraphQL) ---
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

# Parsing metadata for path construction.
PROB_NUM=$(echo "$METADATA" | cut -d'|' -f1)
PROB_NAME=$(echo "$METADATA" | cut -d'|' -f2)
PROB_SLUG=$(echo "$METADATA" | cut -d'|' -f3)

# Calculate directory range (e.g., 242 -> 0201-0300).
START=$(( ( (PROB_NUM - 1) / 100 ) * 100 + 1 ))
END=$(( START + 99 ))
RANGE_DIR=$(printf "%04d-%04d" $START $END)
PROB_DIR=$(printf "%04d. %s" $PROB_NUM "$PROB_NAME")
TARGET_PATH="$RANGE_DIR/$PROB_DIR"

# --- Directory & Description Setup ---
mkdir -p "$TARGET_PATH"
if [ ! -f "$TARGET_PATH/Description.md" ]; then
    # Call the python script using SCRIPT_DIR to ensure it is found.
    python3 "$SCRIPT_DIR/fetch_problem.py" "$PROB_SLUG" --markdown > "$TARGET_PATH/Description.md" 2>/dev/null
    echo "📝 [Created]: Description.md"
else
    echo "ℹ️ [Established]: Description.md already exists."
fi

# --- Template Injection Loop ---
for L in "${CHOSEN_LANGS[@]}"; do
    # Normalize language slugs for the LeetCode API.
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
        echo "⚠️ [Established]: $SUBDIR solution already exists."
    else
        mkdir -p "$TARGET_PATH/$SUBDIR"
        # Injects the official boilerplate code directly into the file.
        python3 "$SCRIPT_DIR/fetch_problem.py" "$PROB_SLUG" --code "$L_SLUG" > "$FILE_PATH"
        echo "✅ [Injected]: $SUBDIR template established."
    fi
done

echo -e "\n🎯 [Service Restored]: Setup complete for $PROB_NAME."