from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates a Sudoku board using Bitmasking to achieve O(1) space 
        and minimal runtime overhead.
        """
        # Instead of using a Set for each row, column, and box, we use 
        # a single integer as a 'Bitmask'. 
        # Since Sudoku only uses digits 1-9, a 9-bit integer is sufficient.
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val_str = board[r][c]
                
                # Pruning: Skip empty cells
                if val_str == ".":
                    continue
                
                # --- Step 1: Bit Position Mapping ---
                # Convert the string digit to an integer and map 1-9 to 0-8.
                # Shift 1 to the left by this value to create a 'mask'.
                # Example: If val is 5, mask is 1 << 4 (binary: 000010000)
                val = int(val_str) - 1
                mask = 1 << val
                
                # --- Step 2: Spatial Mapping (Sub-boxes) ---
                # Map the 2D coordinates (r, c) to a unique 1D box index (0-8).
                box_idx = (r // 3) * 3 + (c // 3)
                
                # --- Step 3: Collision Detection ---
                # Use Bitwise AND (&) to check if the bit at this position is already set.
                # If (rows[r] & mask) > 0, the digit has appeared in this row before.
                if (rows[r] & mask) or (cols[c] & mask) or (boxes[box_idx] & mask):
                    return False
                
                # --- Step 4: State Update ---
                # Use Bitwise OR (|) to set the bit at the current position to 1.
                rows[r] |= mask
                cols[c] |= mask
                boxes[box_idx] |= mask
                
        # If no collisions are detected after a full traversal, the board is valid.
        return True

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: Valid Board
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Example 1 Result: {sol.isValidSudoku(board1)}") # Expected: True

    # Example 2: Invalid Board
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Example 2 Result: {sol.isValidSudoku(board2)}") # Expected: False
