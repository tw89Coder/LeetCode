class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // This will hold the count of non-val elements
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i]; // Copy the non-val element to the front
                k++; // Move the position for the next valid element
            }
        }
        
        return k; // k is the number of elements not equal to val
    }
}
