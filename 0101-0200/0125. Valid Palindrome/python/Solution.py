class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time Complexity:
        - Lowercasing the string: O(n), where n is the length of s.
        - Filtering with str.isalnum and joining: O(n).
        - Reversing the cleaned string and comparing: O(n).
        => Overall: O(n)

        Space Complexity:
        - The cleaned string requires O(n) additional space.
        - The reversed copy also requires O(n).
        => Overall: O(n)
        """
        
        # 1. Normalization: 
        # Convert the entire string to lowercase. This is a single call 
        # to a C-implemented method, making it extremely efficient.
        s = s.lower()
        
        # 2. Functional Filtering:
        # We use 'filter' to remove non-alphanumeric characters.
        # 'filter' is an iterator implemented in C; it is faster than 
        # a list comprehension or a generator expression.
        # "".join() then collects these characters into a new string.
        cleaned = "".join(filter(str.isalnum, s))
        
        # 3. Slicing Comparison:
        # cleaned[::-1] creates a reversed copy of the string using 
        # Python's fast slicing mechanism. 
        # We then perform a direct comparison to check for symmetry.
        return cleaned == cleaned[::-1]

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    
    # Case 1: Complex palindrome with punctuation
    case1 = "A man, a plan, a canal: Panama"
    print(f"Test 1: '{case1}' -> {sol.isPalindrome(case1)}") # Expected: True
    
    # Case 2: Not a palindrome
    case2 = "race a car"
    print(f"Test 2: '{case2}' -> {sol.isPalindrome(case2)}") # Expected: False
    
    # Case 3: Empty/Space input
    case3 = " "
    print(f"Test 3: '{case3}' -> {sol.isPalindrome(case3)}") # Expected: True