import requests
import sys
import re
from bs4 import BeautifulSoup

def clean_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. 先處理行內代碼，這部分很穩定
    for code in soup.find_all('code'):
        code.replace_with(f"`{code.get_text()}`")
    
    # 2. 直接拿取所有文字
    text = soup.get_text(separator='\n')
    
    # 3. 格式化標題（Example 1, Constraints 等）
    text = re.sub(r'Example (\d):', r'## Example \1:', text)
    text = re.sub(r'Constraints:', r'## Constraints:', text)
    
    # 4. 【核心美化邏輯】使用正則表達式處理 Example 區塊
    # 我們尋找從 Input: 開始，直到下一個 ## 或文件結尾的部分
    def beautify_example(match):
        block = match.group(0)
        # 關鍵字加粗
        block = block.replace("Input:", "**Input:**")
        block = block.replace("Output:", "**Output:**")
        block = block.replace("Explanation:", "**Explanation:**")
        
        # 在關鍵字前加入換行，並確保每一行（包括空行）都有 >
        # 先處理換行間距
        block = block.replace("**Output:**", "\n**Output:**")
        block = block.replace("**Explanation:**", "\n**Explanation:**")
        
        # 逐行加上 >
        lines = block.split('\n')
        processed_lines = []
        for line in lines:
            # 即使是空行也要有 > 才會連成一條線
            processed_lines.append(f">{line.strip()}")
        
        return "\n" + "\n".join(processed_lines) + "\n"

    # 這裡的 regex 會抓取從 **Input:** 開始到下一個 ## 標題前的所有內容
    # 我們先處理關鍵字標記，再進行區塊化
    text = re.sub(r'Input:.*?(?=##|$)', beautify_example, text, flags=re.DOTALL)
    
    # 5. 最後清理：移除過多的連續換行
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text.strip()

def format_markdown(prob_id, title, content, difficulty, slug):
    body = clean_content(content)
    return f"""# {prob_id}. {title}
###### tags: `{difficulty}`

{body}

## Complexity Goal:
* **Time**: $O(n)$
* **Space**: $O(n)$

---
[Problem's Link](https://leetcode.com/problems/{slug}/)
"""

def fetch_leetcode_problem(title_slug):
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        difficulty
      }
    }
    """
    try:
        response = requests.post(url, json={'query': query, 'variables': {"titleSlug": title_slug}})
        data = response.json()['data']['question']
        return format_markdown(data['questionId'], data['title'], data['content'], data['difficulty'], title_slug)
    except Exception as e:
        return f"# Error\nCould not fetch problem: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(fetch_leetcode_problem(sys.argv[1]))