import java.util.*;

class Solution {
    public boolean isValid(String s) {
        // 創建一個哈希映射，將開括號對應到閉括號
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        // 創建一個堆疊來存放開括號
        Stack<Character> stackContainer = new Stack<Character>();

        // 遍歷字串中的每個字元
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            
            // 如果是開括號，則將其壓入堆疊
            if (map.containsKey(currentChar)) {
                stackContainer.push(currentChar);
            } else {
                // 如果堆疊是空的（表示目前沒有未匹配的開括號），直接返回 false
                if (stackContainer.empty()) {
                    return false;
                }
                
                // 檢查當前字元是否與堆疊頂部的開括號匹配
                char topElement = stackContainer.peek();
                if (currentChar == map.get(topElement)) {
                    stackContainer.pop(); // 匹配，彈出堆疊頂部的開括號
                } else {
                    return false; // 不匹配，返回 false
                }
            }
        }

        // 最終檢查堆疊是否為空，如果為空表示所有的括號都匹配，返回 true
        return stackContainer.empty();
    }
}
