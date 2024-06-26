import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numOfIndex = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            // 檢查HashMap中是否存在與當前元素之和為目標值的另一個元素
            // target - nums[i] 計算需要配對的另一個數
            if (numOfIndex.containsKey(target - nums[i])) { 
                return new int[] {numOfIndex.get(target - nums[i]), i};
            }
            // 如果不存在，將當前元素及其索引存入HashMap
            numOfIndex.put(nums[i], i);
        }
        return new int[] {};
    }
}