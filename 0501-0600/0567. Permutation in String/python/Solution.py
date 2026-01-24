class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Main Idea:
        Two strings are permutations if their character frequencies are identical. 
        We use a fixed-size sliding window of length len(s1) across s2. 
        
        Optimizations:
        1. Pre-convert characters to integers to avoid repetitive ord() calls.
        2. Utilize Python's internal list comparison (L1 == L2), which is 
           implemented in C and is faster than manual match-counting in Python.

        Complexity:
            Time: O(n2) - Single pass with optimized bulk comparisons.
            Space: O(n1 + n2) - Auxiliary integer index storage.
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # Fixed frequency arrays for 26 lowercase English letters
        target = [0] * 26
        window = [0] * 26
        a_ord = ord('a')
        
        # Performance: Pre-convert strings to integer indices [0-25]
        # This removes the function call overhead of ord() from the main loop.
        s1_indices = [ord(c) - a_ord for c in s1]
        s2_indices = [ord(c) - a_ord for c in s2]
        
        # Initialize the target frequency and the first sliding window
        for i in range(n1):
            target[s1_indices[i]] += 1
            window[s2_indices[i]] += 1
            
        # Initial check for the first window
        if target == window:
            return True
            
        # Slide the window through s2_indices
        for i in range(n1, n2):
            # Update window frequency: Add the entering char, remove the exiting char
            window[s2_indices[i]] += 1
            window[s2_indices[i - n1]] -= 1
            
            # Optimization: List comparison in Python is highly optimized at 
            # the bytecode level, outperforming manual 'match' increments.
            if window == target:
                return True
                
        return False

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test Case 1: {sol.checkInclusion('ab', 'eidbaooo')}") # True
    print(f"Test Case 2: {sol.checkInclusion('ab', 'eidboaoo')}") # False