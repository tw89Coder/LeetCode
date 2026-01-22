from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Main Idea:
        Instead of calculating the width by looking back at the stack after popping, 
        we track the 'start index' for each height. When a height is popped, its 
        total width is (current_index - start_index). This minimizes list lookups 
        and arithmetic operations inside the loop.

        Complexity:
            Time: O(n) - Single pass with constant time operations.
            Space: O(n) - Auxiliary stack to store (index, height) pairs.
        """
        max_area = 0
        stack = [] # Stores pairs: (start_index, height)
        
        # Localize stack methods for a small performance boost
        push = stack.append
        pop = stack.pop

        for i, h in enumerate(heights):
            # We assume the current height starts at its current index
            start = i
            
            # When we find a shorter height, we trigger the area calculation 
            # for all taller heights currently in the stack.
            while stack and stack[-1][1] >= h:
                # Pop the height and its starting index
                index, height = pop()
                # Calculate area: the height can span from its 'index' up to 'i'
                area = height * (i - index)
                if area > max_area:
                    max_area = area
                # The current shorter height 'h' can extend back to the 
                # 'index' of the taller height we just popped.
                start = index
            
            # Push the current height and its adjusted starting index
            push((start, h))

        # After the loop, process any remaining bars in the stack.
        # These bars extend all the way to the right end of the histogram.
        n = len(heights)
        for index, height in stack:
            area = height * (n - index)
            if area > max_area:
                max_area = area
                
        return max_area

# --- Standalone Test ---
if __name__ == "__main__":
    sol = Solution()
    # Test case: [2,1,5,6,2,3] -> Expected result 10
    print(f"Largest Area: {sol.largestRectangleArea([2, 1, 5, 6, 2, 3])}")