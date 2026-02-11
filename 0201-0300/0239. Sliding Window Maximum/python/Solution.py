from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Main Idea:
        - Use a Monotonic Decreasing Queue (Deque) to store indices of potential maximums.
        - The front of the deque (dq[0]) always holds the index of the maximum value for the current window.
        - As the window slides:
            1. Remove indices from the front that are out of the current window range.
            2. Remove indices from the back if their values are smaller than the current element 
               (maintain decreasing order).
            3. Add the current element's index.
            4. Record the maximum (value at dq[0]) to the result.

        Time and Space Complexity:
        - Time: O(N)
          Each element is added to the deque once and removed at most once. Amortized time is linear.
        - Space: O(k)
          The deque stores at most k indices in the worst case.
        """
        if k == 1: return nums
        n = len(nums)
        if n == 0: return []
        
        # Optimization: Pre-allocate result list to avoid dynamic resizing overhead
        res = [0] * (n - k + 1)
        dq = deque()
        
        # Optimization: Localize deque methods to reduce attribute lookup time in Python loops
        pop = dq.pop
        popleft = dq.popleft
        append = dq.append
        
        # Process the first window (first k elements)
        for i in range(k):
            # Maintain monotonic decreasing order: pop smaller elements from the back
            while dq and nums[i] >= nums[dq[-1]]:
                pop()
            append(i)
        
        # The max of the first window is at the front of the deque
        res[0] = nums[dq[0]]
        
        # Process the rest of the array
        for i in range(k, n):
            # 1. Remove the front element if it's out of the current window [i-k+1, i]
            if dq[0] <= i - k:
                popleft()
            
            # 2. Maintain monotonic decreasing order
            while dq and nums[i] >= nums[dq[-1]]:
                pop()
            
            # 3. Add current index
            append(i)
            
            # 4. Record the max value for the current window
            res[i - k + 1] = nums[dq[0]]
            
        return res