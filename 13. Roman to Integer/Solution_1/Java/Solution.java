import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        int result = 0;

        if (!s.isEmpty()) {
            HashMap<Character,Integer> map = new HashMap<Character,Integer>();
            map.put('I', 1);
            map.put('V', 5);
            map.put('X', 10);
            map.put('L', 50);
            map.put('C', 100);
            map.put('D', 500);
            map.put('M', 1000);
        
            // 遍歷字符串
            for (int i = 0; i < s.length(); i++) {
                // 獲取當前字符對應的值
                int current = map.get(s.charAt(i));
                // 如果不是最後一個字符，並且當前字符的值小於下一個字符的值，則需要減去當前值
                if (i < s.length() - 1 && current < map.get(s.charAt(i + 1))) {
                    result -= current;
                } else {
                    // 否則加上當前值
                    result += current;
                }
            }
        }

        return result;
    }
}