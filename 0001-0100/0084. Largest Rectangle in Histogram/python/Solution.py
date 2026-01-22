from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Main Idea:
        Use a monotonic increasing stack to track indices of heights. When we 
        encounter a height smaller than the stack's top, it means the rectangle 
        using the stack top's height as its minimum height has reached its 
        right boundary. The new stack top after popping is its left boundary.

        Complexity:
            Time: O(n) - Linear pass through heights.
            Space: O(n) - Stack stores indices.
        """
        # Step 1: Add sentinel 0s to handle edge cases and empty the stack at the end.
        # The 0 at the start simplifies width calculation (left boundary).
        # The 0 at the end forces all remaining elements out of the stack.
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        
        # Localize method references for performance tuning
        pop = stack.pop
        push = stack.append

        for i, h in enumerate(heights):
            # Step 2: While the current height is smaller than the height at stack top.
            # This maintains the "monotonic increasing" property.
            while stack and h < heights[stack[-1]]:
                # The height of the rectangle we are calculating now.
                height = heights[pop()]
                
                # Step 3: Determine the width.
                # After popping, the current stack[-1] is the left boundary (exclusive).
                # 'i' is the right boundary (exclusive).
                # Width = (right - left - 1)
                width = i - stack[-1] - 1
                
                area = height * width
                if area > max_area:
                    max_area = area
            
            # Step 4: Push current index onto stack.
            push(i)
            
        return max_area

# --- Standalone Test Execution ---
if __name__ == "__main__":
    sol = Solution()
    # Example 1: [2, 1, 5, 6, 2, 3] -> Expected 10
    print(f"Max Area: {sol.largestRectangleArea([2, 1, 5, 6, 2, 3])}")