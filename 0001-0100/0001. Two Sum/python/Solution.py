from typing import List

class Solution:
    """
    Problem: Two Sum (LeetCode 1).
    Goal: Find two indices such that their corresponding values sum up to 'target'.
    
    Approach: Single-pass Hash Map.
    Time Complexity: O(n) - We traverse the list once. Hash map lookups are O(1) on average.
    Space Complexity: O(n) - In the worst case, we store nearly all elements in the dictionary.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 'prev_map' stores 'value: index' pairs of elements we have already visited.
        # This allows us to look back and find the complement of the current number in O(1).
        prev_map = {}
        
        # Performance optimization: Cache the length to avoid repeated len() calls 
        # inside the loop, though CPython often optimizes this internally.
        num_elements = len(nums)
        
        # We use a standard range loop to minimize Python object creation 
        # (avoiding the tuple unpacking overhead found in enumerate()).
        for i in range(num_elements):
            current_val = nums[i]
            
            # The value we need to find to satisfy the equation: current_val + complement = target
            complement = target - current_val
            
            # Check if the complement exists in our 'seen' collection.
            # Using the 'in' operator on a dict is a highly optimized C-level operation (hash lookup).
            if complement in prev_map:
                # Return the index of the complement and the current index.
                # This guarantees we don't use the same element twice.
                return [prev_map[complement], i]
            
            # If the complement is not found, record the current value and its index.
            # This 'memorization' allows future elements to find this value.
            prev_map[current_val] = i
            
        # Per problem constraints, a solution always exists, so this line is rarely reached.
        return []

# --- Standard Test Suite ---
if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case
    # Explanation: 2 + 7 = 9. Indices are [0, 1]
    assert sorted(solver.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    
    # Test Case 2: Indices are not at the start
    # Explanation: 2 + 4 = 6. Indices are [1, 2]
    assert sorted(solver.twoSum([3, 2, 4], 6)) == [1, 2]
    
    # Test Case 3: Duplicate values
    # Explanation: 3 + 3 = 6. Indices are [0, 1]
    assert sorted(solver.twoSum([3, 3], 6)) == [0, 1]
    
    print("All professional test cases passed successfully.")