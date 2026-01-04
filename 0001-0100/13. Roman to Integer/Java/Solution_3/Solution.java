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
        int prev = 0;

        // 從右向左遍歷字符串
        for (int i = s.length() - 1; i >= 0; i--) {
            int current = values[s.charAt(i) - 'A'];

            // 如果當前值小於之前的值，則減去當前值，否則加上當前值
            if (current < prev) {
                result -= current;
            } else {
                result += current;
            }

            // 更新之前的值
            prev = current;
        }

        return result;
    }
}