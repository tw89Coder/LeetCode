import java.util.*;

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        Stack<Character> stackContainer = new Stack<Character>();
        for (int i = 0; i < s.length; i++) {
            if (map.containsKey(s.charAt(i))) { 
                stackContainer.push(s.charAt(i));
            }
            // 如果不存在，將當前元素及其索引存入HashMap
            map.put(nums[i], i);
        }
        return new int[] {};
    }
}