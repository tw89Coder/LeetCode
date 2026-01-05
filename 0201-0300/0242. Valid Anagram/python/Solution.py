class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Quick length check (O(1))
        if len(s) != len(t):
            return False
            
        # 2. Check counts of unique characters only
        # This uses highly optimized C-level string.count()
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1, t1 = "anagram", "nagaram"
    res1 = sol.isAnagram(s1, t1)
    print(f"Test Case 1: s='{s1}', t='{t1}'")
    print(f"Expected: True | Result: {res1}\n")
    
    # Example 2
    s2, t2 = "rat", "car"
    res2 = sol.isAnagram(s2, t2)
    print(f"Test Case 2: s='{s2}', t='{t2}'")
    print(f"Expected: False | Result: {res2}")