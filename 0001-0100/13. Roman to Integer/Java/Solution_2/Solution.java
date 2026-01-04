class Solution {
    public int romanToInt(String s) {
        // 創建一個陣列來存儲羅馬數字字符對應的整數值
        int[] values = new int[26];
        values['I' - 'A'] = 1;
        values['V' - 'A'] = 5;
        values['X' - 'A'] = 10;
        values['L' - 'A'] = 50;
        values['C' - 'A'] = 100;
        values['D' - 'A'] = 500;
        values['M' - 'A'] = 1000;

        int result = 0;
        int length = s.length();

        // 遍歷字符串
        for (int i = 0; i < length; i++) {
            int current = values[s.charAt(i) - 'A'];
            // 如果不是最後一個字符，並且當前字符的值小於下一個字符的值，則需要減去當前值
            if (i < length - 1 && current < values[s.charAt(i + 1) - 'A']) {
                result -= current;
            } else {
                // 否則加上當前值
                result += current;
            }
        }

        return result;
    }
}
