from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements except nums[i] in O(n) time.
        This approach avoids the division operator and minimizes auxiliary space.
        """
        n = len(nums)
        # Initialize the result array. 
        # In complexity analysis, the output array is usually not counted as extra space.
        res = [1] * n
        
        # --- First Pass: Calculate Prefix Products ---
        # The 'curr' variable acts as an accumulator for the products of all 
        # elements strictly to the left of the current index 'i'.
        curr = 1
        for i in range(n):
            # Assign the accumulated prefix product to the current position
            res[i] = curr
            # Update the accumulator by multiplying it with the current element
            curr *= nums[i]
            
        # --- Second Pass: Calculate Postfix (Suffix) Products ---
        # We traverse the array in reverse. Now, 'curr' accumulates the products 
        # of all elements strictly to the right of the current index 'i'.
        curr = 1
        for i in range(n - 1, -1, -1):
            # Multiply the existing prefix product by the newly calculated postfix product
            res[i] *= curr
            # Update the accumulator for the next iteration to the left
            curr *= nums[i]
            
        return res

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard positive integers
    nums1 = [1, 2, 3, 4]
    # Prefix: [1, 1, 2, 6]
    # Postfix: [24, 12, 4, 1]
    # Result: [24, 12, 8, 6]
    print(f"Test 1 - Input: {nums1} | Output: {sol.productExceptSelf(nums1)}")
    
    # Test Case 2: Handling zeros
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Test 2 - Input: {nums2} | Output: {sol.productExceptSelf(nums2)}")
    
    # Automated Integrity Check
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    print("\nStatus: All test cases passed with O(n) efficiency.")