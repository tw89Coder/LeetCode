class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Extreme Optimization for Python:
        1. Use bytearray (s.encode()) to treat characters as integers (0-128).
        2. Replace dictionary with a fixed-size list for O(1) direct indexing.
        3. Filter only relevant indices to reduce iterations.
        
        Complexity:
            Time: O(m + n)
            Space: O(m + n)
        """
        n, m = len(s), len(t)
        if n < m: return ""

        # Step 1: Encode to bytes (integers) for faster access
        s_bytes = s.encode()
        t_bytes = t.encode()

        # Step 2: Use fixed-size arrays for frequencies (ASCII size 128)
        target_count = [0] * 128
        for b in t_bytes:
            target_count[b] += 1
        
        # Number of unique characters in t that must be satisfied
        required = sum(1 for i in range(128) if target_count[i] > 0)
        
        # Step 3: Pre-filter indices of s that are present in t
        # This drastically reduces the search space
        filtered = [i for i, b in enumerate(s_bytes) if target_count[b] > 0]
        
        l, r = 0, 0
        formed = 0
        window_count = [0] * 128
        min_len = n + 1
        res = (0, 0) # Store (start, end) indices

        # Step 4: Optimized Sliding Window
        while r < len(filtered):
            # Use index and pre-encoded byte value
            idx_r = filtered[r]
            char_r = s_bytes[idx_r]
            window_count[char_r] += 1
            
            if window_count[char_r] == target_count[char_r]:
                formed += 1
            
            # Shrink the window when valid
            while formed == required:
                idx_l = filtered[l]
                char_l = s_bytes[idx_l]
                
                # Update result
                current_len = idx_r - idx_l + 1
                if current_len < min_len:
                    min_len = current_len
                    res = (idx_l, idx_r)
                
                # Pop character from the left
                window_count[char_l] -= 1
                if window_count[char_l] < target_count[char_l]:
                    formed -= 1
                l += 1
            
            r += 1
            
        return "" if min_len > n else s[res[0]:res[1]+1]

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    # Example 1: s = "ADOBECODEBANC", t = "ABC" -> "BANC"
    print(f"Result: {sol.minWindow('ADOBECODEBANC', 'ABC')}")