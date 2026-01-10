from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Calculates the length of the longest consecutive sequence in O(n) time.
        
        This implementation is optimized for CPython by reducing bytecode 
        execution overhead and minimizing redundant arithmetic operations.
        """
        # --- Edge Case Handling ---
        # An empty input array has a maximum consecutive streak of 0.
        if not nums:
            return 0
        
        # --- Data Structure Initialization ---
        # Convert the list to a Hash Set for O(1) average-time complexity lookups.
        # This also automatically handles duplicate elements.
        num_set = set(nums)
        longest_streak = 0
        
        # --- Linear Traversal ---
        # We iterate over the set rather than the original list to avoid 
        # redundant processing of duplicates.
        for n in num_set:
            
            # --- Sequence Start Identification (Pruning) ---
            # We only initiate a search if 'n' is the absolute minimum 
            # of a potential sequence (i.e., 'n - 1' is not present).
            # This ensures each element is visited at most twice (O(2n) total).
            if (n - 1) not in num_set:
                
                # --- Forward Probing ---
                # Initialize a probe pointer 'm' at the next integer.
                m = n + 1
                
                # Use a localized 'while' loop to find the end of the sequence.
                # In CPython, accessing local variables is faster than 
                # repeated object attribute or complex expression evaluation.
                while m in num_set:
                    m += 1
                
                # --- Result Calculation ---
                # The length is the distance between the final probe 'm' 
                # and the sequence start 'n'.
                # streak = current_end - start
                streak = m - n
                
                # Manual comparison is often faster than calling max() 
                # in performance-critical Python code due to function call overhead.
                if streak > longest_streak:
                    longest_streak = streak
                    
        return longest_streak

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: Standard case
    test1 = [100, 4, 200, 1, 3, 2]
    # Sequence [1, 2, 3, 4] -> length 4
    print(f"Test 1 - Input: {test1} | Output: {sol.longestConsecutive(test1)}")
    
    # Example 2: Multiple sequences and duplicates
    test2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # Sequence [0, 1, 2, 3, 4, 5, 6, 7, 8] -> length 9
    print(f"Test 2 - Input: {test2} | Output: {sol.longestConsecutive(test2)}")

    assert sol.longestConsecutive(test1) == 4
    print("\nStatus: O(n) Logic Verified.")