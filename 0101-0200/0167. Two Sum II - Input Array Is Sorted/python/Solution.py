from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Hybrid Approach: Converging Two-Pointer with Binary Search Acceleration.
        
        Time Complexity:
            - Average/Best: O(log n) due to logarithmic jumps in sparse data.
            - Worst: O(n) when jumps are minimal, but with low constant factor.
            
        Space Complexity:
            - O(1) auxiliary space as only constant pointers are maintained.
        """
        n = len(numbers)
        left = 0
        right = n - 1
        
        # Initial search space reduction using C-optimized binary search
        right = bisect.bisect_right(numbers, target - numbers[left], lo = left + 1, hi = right)
        if right == n: 
            right = n - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            
            elif current_sum < target:
                # O(log n) jump for the lower bound
                left = bisect.bisect_left(numbers, target - numbers[right], lo = left + 1, hi = right)
            else:
                # O(log n) jump for the upper bound
                right = bisect.bisect_right(numbers, target - numbers[left], lo = left, hi = right - 1)
                if right > 0 and numbers[right] > target - numbers[left]:
                    right -= 1
                    
        return []

# --- Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums = [2, 7, 11, 15]
    t = 9
    print(f"Input: {nums}, target: {t} | Output: {sol.twoSum(nums, t)}") # Expected: [1, 2]