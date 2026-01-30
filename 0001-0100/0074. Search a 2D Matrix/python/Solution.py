from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Main Idea:
        Treat the m x n matrix as a virtual 1D sorted array of length m*n.
        Convert the 1D index 'mid' back to 2D coordinates (r, c) using:
        r = mid // n
        c = mid % n

        Complexity:
            Time: O(log(m * n))
            Space: O(1)
        """
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Coordinate conversion: 1D index to 2D row/col
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

# --- Test Script ---
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(f"Target 3 found: {sol.searchMatrix(matrix, 3)}")   # True
    print(f"Target 13 found: {sol.searchMatrix(matrix, 13)}") # False