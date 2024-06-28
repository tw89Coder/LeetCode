class Solution {
    public int romanToInt(String s) {
        int result = 0;

        if (!s.isEmpty()) {
            HashMap<String,Integer> map = new HashMap<String,Integer>();
            map.put("I", 1);
            map.put("V", 5);
            map.put("X", 10);
            map.put("L", 50);
            map.put("C", 100);
            map.put("D", 500);
            map.put("M", 1000);

        }

        return result;
    }
}