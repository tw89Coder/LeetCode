class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Main Idea:
        A permutation of s1 in s2 means a substring of s2 has the same character 
        counts as s1. We use a sliding window of size len(s1) and a matches counter 
         to track how many characters (out of 26) have identical counts.
        
        Complexity:
            Time: O(n) - Linear pass through s2.
            Space: O(1) - Fixed size array (26 lowercase letters).
        """
        if len(s1) > len(s2):
            return False

        # Use arrays instead of dicts for faster access (0-25 for a-z)
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Count initial matches across 26 characters
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # Slide the window across s2
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Logic for adding the right character
            idx = ord(s2[right]) - ord('a')
            s2_count[idx] += 1
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            elif s1_count[idx] + 1 == s2_count[idx]:
                matches -= 1

            # Logic for removing the left character
            idx = ord(s2[left]) - ord('a')
            s2_count[idx] -= 1
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            elif s1_count[idx] - 1 == s2_count[idx]:
                matches -= 1
            
            left += 1

        return matches == 26

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test Case 1: {sol.checkInclusion('ab', 'eidbaooo')}") # True
    print(f"Test Case 2: {sol.checkInclusion('ab', 'eidboaoo')}") # False