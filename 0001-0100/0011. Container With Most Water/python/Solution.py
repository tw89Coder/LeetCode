from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Main Idea:
        The container capacity is limited by the shorter of the two vertical lines.
        Using a two-pointer approach, we start from the widest possible container 
        and strategically move inward. To potentially increase the area, we must 
        find a taller bar by moving the pointer that points to the shorter line. 
        We skip redundant bars that are shorter than the current boundaries 
        to minimize area calculations.

        Complexity:
            Time: O(n) - Each element is processed at most once.
            Space: O(1) - Constant auxiliary memory usage.
        """
        # Pointer Initialization: Starting at the maximum possible width.
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Step 1: Cache local heights to minimize repeated array access.
            h_l = height[left]
            h_r = height[right]
            
            # Step 2: Calculate area and move pointers.
            # The 'bottleneck' is always the shorter bar.
            if h_l < h_r:
                current_area = h_l * (right - left)
                # Skip bars from the left that cannot increase the height limit.
                while left < right and height[left] <= h_l:
                    left += 1
            else:
                current_area = h_r * (right - left)
                # Skip bars from the right that cannot increase the height limit.
                while left < right and height[right] <= h_r:
                    right -= 1
            
            # Step 3: Update global maximum using inline comparison for speed.
            if current_area > max_area:
                max_area = current_area
                
        return max_area

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    test_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Process: 
    # Starts with (1, 7) -> moves left (1 is shorter)
    # Eventually finds (8, 7) at indices 1 and 8 -> Area: 7 * (8-1) = 49
    print(f"Max Water Container Area: {sol.maxArea(test_heights)}")