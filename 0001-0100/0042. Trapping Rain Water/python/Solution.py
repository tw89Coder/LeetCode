from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Main Idea:
        The water trapped at any bar depends on the lower of the two boundary 
        peaks. Instead of checking the boundary condition for every single bar, 
        we identify the lower side (bottleneck) and use an inner loop to 
        process all subsequent bars on that slope until we hit a new peak. 
        This minimizes branch evaluations in the Python interpreter.

        Complexity:
            Time: O(n) - Linear pass with reduced constant-time operations.
            Space: O(1) - Constant auxiliary variables.
        """
        if not height:
            return 0
        
        # Initialize pointers and record the initial boundary peaks
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        
        while left < right:
            # Determine which side is the 'bottleneck' (the limiting wall)
            if left_max < right_max:
                left += 1
                # --- INNER SKIP LOOP (Left) ---
                # As long as the current bars are lower than left_max, 
                # they are guaranteed to trap water up to the left_max level.
                # This bypasses the 'if left_max < right_max' check for these bars.
                while left < right and height[left] < left_max:
                    total_water += left_max - height[left]
                    left += 1
                # Update the new peak on the left side
                left_max = height[left]
            else:
                right -= 1
                # --- INNER SKIP LOOP (Right) ---
                # Similarly, process the right slope if right_max is the bottleneck.
                while left < right and height[right] < right_max:
                    total_water += right_max - height[right]
                    right -= 1
                # Update the new peak on the right side
                right_max = height[right]
                
        return total_water

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    test_h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # Expect 6 units of water
    print(f"Trapped Water: {sol.trap(test_h)}")