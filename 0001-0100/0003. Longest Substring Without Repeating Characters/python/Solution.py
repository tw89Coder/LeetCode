class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Main Idea:
        Use a sliding window with a Hash Map to store the last seen index 
        of each character. This allows the 'left' pointer to jump directly 
        to a safe position when a duplicate is found.
        
        Complexity:
            Time: O(n) - Single pass through the string.
            Space: O(min(m, n)) - Hash map for character indexing.
        """
        char_map = {} # char -> last_seen_index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If the character is already in the map and within the current window
            if char in char_map and char_map[char] >= left:
                # Jump the left pointer to the position after the last occurrence
                left = char_map[char] + 1
            
            # Update the character's latest position
            char_map[char] = right
            
            # Calculate the window size and update global maximum
            # inline comparison is faster than max() function in Python
            current_len = right - left + 1
            if current_len > max_length:
                max_length = current_len
                
        return max_length

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Result 'abcabcbb': {sol.lengthOfLongestSubstring('abcabcbb')}") # 3
    print(f"Result 'pwwkew':   {sol.lengthOfLongestSubstring('pwwkew')}")   # 3