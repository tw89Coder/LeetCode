from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Assign each lowercase English letter a unique prime number.
        # This ensures that the product of primes for any anagram will be identical,
        # since multiplication is commutative and prime factorization is unique.
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
            31, 37, 41, 43, 47, 53, 59, 61, 67, 
            71, 73, 79, 83, 89, 97, 101
        ]
        
        # Use a dictionary to group words by their prime product key.
        ans = defaultdict(list)
        
        for s in strs:
            key = 1
            # Compute the product of primes corresponding to each character in the string.
            # All anagrams will yield the same product, serving as a unique identifier.
            for char in s:
                key *= primes[ord(char) - ord('a')]
            # Append the word to the group identified by this key.
            ans[key].append(s)
        
        # Return all grouped anagrams as a list of lists.
        return list(ans.values())

# --- Testing Block ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Multiple anagram groups
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Test Case 1 Input: {input1}")
    print(f"Output: {sol.groupAnagrams(input1)}")
    # Expected: [["eat","tea","ate"],["tan","nat"],["bat"]] (Order may vary)

    # Test Case 2: Empty string
    input2 = [""]
    print(f"\nTest Case 2 Input: {input2}")
    print(f"Output: {sol.groupAnagrams(input2)}")
    # Expected: [[""]]

    # Test Case 3: Single character
    input3 = ["a"]
    print(f"\nTest Case 3 Input: {input3}")
    print(f"Output: {sol.groupAnagrams(input3)}")
    # Expected: [["a"]]