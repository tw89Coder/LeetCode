from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Main Idea:
        Maintain a sliding window and track the frequency of each character 
        within it. If (Window Length - Max Frequency) > k, the window is 
        invalid, and we shrink it from the left.
        
        Complexity:
            Time: O(n) - Single pass through the string.
            Space: O(1) - Frequency map capped at 26 characters.
        """
        count = {}
        max_freq = 0
        left = 0
        max_length = 0
        
        # 'right' expands the window
        for right in range(len(s)):
            char = s[right]
            count[char] = 1 + count.get(char, 0)
            
            # Update the frequency of the most common character seen so far.
            # Optimization: We don't need to decrease max_freq when shrinking
            # because the result only improves if we find a larger max_freq.
            if count[char] > max_freq:
                max_freq = count[char]
            
            # Calculate current window length
            window_len = right - left + 1
            
            # If the number of characters to replace exceeds k, shrink the window
            if window_len - max_freq > k:
                # Decrease the count of the character leaving the window
                count[s[left]] -= 1
                left += 1
            else:
                # Only update max_length if the current window is valid
                if window_len > max_length:
                    max_length = window_len
                    
        return max_length

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    # Example 1: "ABAB", k = 2 -> Result: 4
    print(f"Test 'ABAB': {sol.characterReplacement('ABAB', 2)}")
    # Example 2: "AABABBA", k = 1 -> Result: 4
    print(f"Test 'AABABBA': {sol.characterReplacement('AABABBA', 1)}")