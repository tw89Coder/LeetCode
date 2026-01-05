import requests
import sys
import re
from bs4 import BeautifulSoup

def clean_content(html_content):
    """
    Converts LeetCode HTML description into clean Markdown with blockquotes.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    for code in soup.find_all('code'):
        code.replace_with(f"`{code.get_text()}`")
    
    text = soup.get_text(separator='\n')
    text = re.sub(r'Example (\d):', r'## Example \1:', text)
    text = re.sub(r'Constraints:', r'## Constraints:', text)
    
    def beautify_example(match):
        block = match.group(0)
        block = block.replace("Input:", "**Input:**").replace("Output:", "**Output:**").replace("Explanation:", "**Explanation:**")
        block = block.replace("**Output:**", "\n**Output:**").replace("**Explanation:**", "\n**Explanation:**")
        lines = block.split('\n')
        processed_lines = [f">{line.strip()}" for line in lines]
        return "\n" + "\n".join(processed_lines) + "\n"

    text = re.sub(r'Input:.*?(?=##|$)', beautify_example, text, flags=re.DOTALL)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()

def fetch_leetcode_data(title_slug):
    """
    Fetches both problem content and code snippets via GraphQL.
    """
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        difficulty
        codeSnippets {
          langSlug
          code
        }
      }
    }
    """
    try:
        response = requests.post(url, json={'query': query, 'variables': {"titleSlug": title_slug}})
        return response.json()['data']['question']
    except Exception:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    slug = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "--markdown"
    
    data = fetch_leetcode_data(slug)
    if not data:
        sys.exit(1)

    if mode == "--markdown":
        body = clean_content(data['content'])
        print(f"# {data['questionId']}. {data['title']}\n###### tags: `{data['difficulty']}`\n\n{body}\n\n## Complexity Goal:\n* **Time**: $O(n)$\n* **Space**: $O(n)$\n\n---\n[Problem Link](https://leetcode.com/problems/{slug}/)")
    
    elif mode == "--code" and len(sys.argv) > 3:
        target_lang = sys.argv[3]
        snippet = next((s['code'] for s in data['codeSnippets'] if s['langSlug'] == target_lang), "")
        print(snippet)