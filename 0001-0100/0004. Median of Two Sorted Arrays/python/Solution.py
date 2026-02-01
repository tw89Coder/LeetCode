from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Main Idea:
            - The problem asks for the median of two sorted arrays, which is equivalent to finding 
              the correct partition that splits the combined set into two halves of equal length.
            - We perform a Binary Search on the smaller array to find a partition index `i`.
            - Based on `i`, we calculate the corresponding partition index `j` in the second array.
            - The correct partition must satisfy:
                max(left_part) <= min(right_part)
              Specifically: nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i].

        Time and Space Complexity:
            - Time: O(log(min(m, n)))
              We strictly perform binary search on the shorter array (length m), minimizing the search space.
            - Space: O(1)
              We only store a constant number of variables (indices and boundary values), using no extra data structures.
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)
        
        # Ensure A is the smaller array to minimize the binary search range (O(log(min(m, n))))
        if m > n:
            A, B, m, n = B, A, n, m
            
        left, right = 0, m
        # Calculate half length using bitwise shift (equivalent to // 2)
        half_len = (m + n + 1) >> 1
        
        # Define infinity boundaries for edge cases (based on problem constraints)
        INF = 10**7
        NEG_INF = -10**7
        
        while left <= right:
            # i is the partition index in A, j is the partition index in B
            i = (left + right) >> 1
            j = half_len - i
            
            # Handle edge cases where the partition falls at the beginning or end of an array.
            # Use ternary operators to assign boundary values efficiently.
            aleft = A[i-1] if i > 0 else NEG_INF
            aright = A[i] if i < m else INF
            bleft = B[j-1] if j > 0 else NEG_INF
            bright = B[j] if j < n else INF
            
            # Check if we found the correct partition
            if aleft <= bright and bleft <= aright:
                # If the total length is odd, the median is the maximum of the left side.
                if (m + n) & 1: 
                    return float(aleft if aleft > bleft else bleft)
                # If the total length is even, the median is the average of the max-left and min-right.
                else:
                    l_max = aleft if aleft > bleft else bleft
                    r_min = aright if aright < bright else bright
                    return (l_max + r_min) / 2.0
            
            # If A's left part is too large, move the partition to the left
            elif aleft > bright:
                right = i - 1
            # If A's left part is too small, move the partition to the right
            else:
                left = i + 1
                
        return 0.0

# --- Test Script ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Median of [1,3] and [2]: {sol.findMedianSortedArrays([1,3], [2])}") # 2.0
    print(f"Median of [1,2] and [3,4]: {sol.findMedianSortedArrays([1,2], [3,4])}") # 2.5