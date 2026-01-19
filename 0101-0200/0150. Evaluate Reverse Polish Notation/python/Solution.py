from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Main Idea:
        Evaluate the RPN expression using a stack with optimized method lookups.
        We use local variable caching for stack operations and Python 3.10's 
        match-case for faster branching. Truncation toward zero is handled 
        via int(a / b).

        Complexity:
            Time: O(n) - Single pass with optimized constant overhead.
            Space: O(n) - Auxiliary stack storage.
        """
        stack = []
        # Caching methods to local variables saves attribute lookup time per call
        push = stack.append
        pop = stack.pop
        
        for token in tokens:
            match token:
                case "+":
                    # Order is irrelevant for addition
                    push(pop() + pop())
                case "-":
                    # Order matters: second pop is the left operand
                    b = pop()
                    a = pop()
                    push(a - b)
                case "*":
                    # Order is irrelevant for multiplication
                    push(pop() * pop())
                case "/":
                    # Order matters: second pop is the left operand
                    b = pop()
                    a = pop()
                    # int() on float division results in truncation toward zero
                    push(int(a / b))
                case _:
                    # If not an operator, convert string to integer and push
                    push(int(token))
                    
        return stack[0]

# --- Testing Script ---
if __name__ == "__main__":
    sol = Solution()
    # Case: ((10 * (6 / -132)) + 17) + 5
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f"RPN Result: {sol.evalRPN(tokens)}") # Expected: 22