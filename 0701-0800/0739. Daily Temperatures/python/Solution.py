from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Main Idea:
        Use a Monotonic Decreasing Stack to store indices of days for which we 
        haven't found a warmer temperature yet. When we encounter a day that is 
        warmer than the day at the stack's top, we calculate the difference 
        in days and pop the index.

        Complexity:
            Time: O(n) - Each element is pushed and popped at most once.
            Space: O(n) - To store the indices in the stack.
        """
        n = len(temperatures)
        # Initialize the result array with 0s. 
        # If no warmer day is found, it remains 0 by default.
        ans = [0] * n
        stack = [] # This will store the indices (not the temperatures)

        # Caching the pop and append methods for slight performance gain
        pop = stack.pop
        push = stack.append

        for i, temp in enumerate(temperatures):
            # While stack is not empty and current temp is warmer than the 
            # temperature at the index stored at the top of the stack.
            while stack and temp > temperatures[stack[-1]]:
                prev_index = pop()
                # Calculate the waiting days
                ans[prev_index] = i - prev_index
            
            # Push the current day's index onto the stack
            push(i)
            
        return ans

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    test_temps = [73, 74, 75, 71, 69, 72, 76, 73]
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(f"Waiting Days: {sol.dailyTemperatures(test_temps)}")