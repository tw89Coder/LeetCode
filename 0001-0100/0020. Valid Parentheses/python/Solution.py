class Solution:
    def isValid(self, s: str) -> bool:
        """
        Main Idea:
        Use a Stack to keep track of the opening brackets. Because the 
        most recently opened bracket must be the first one to be closed 
        (LIFO), a Stack is the ideal data structure for this problem.

        Complexity:
            Time: O(n) - Single pass through the string.
            Space: O(n) - Maximum stack size scales with input length.
        """
        # Map closing brackets to their corresponding opening brackets.
        # This makes the matching logic much cleaner and faster.
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, 
                # otherwise assign a dummy value '#' that won't match.
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the required one.
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack.
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly.
        return not stack

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test '()[]{{}}': {sol.isValid('()[]{}')}") # Expected: True
    print(f"Test '([)]':     {sol.isValid('([)]')}")   # Expected: False
    print(f"Test '([])':     {sol.isValid('([])')}")   # Expected: True