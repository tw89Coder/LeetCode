class MinStack:
    """
    Main Idea:
    Maintain a primary stack for data storage and a secondary auxiliary stack 
    (min_stack) to track the minimum values. To optimize space and performance, 
    the auxiliary stack only records a new value when the pushed element is 
    less than or equal to the current minimum. This ensures that the top of 
    min_stack always provides the minimum element in O(1) time.
    
    Complexity:
        Time: O(1) for all methods.
        Space: O(n) worst-case.
    """

    def __init__(self):
        """
        Initialize the data structures.
        """
        # Primary stack to store all pushed elements
        self.stack = []
        # Auxiliary stack to store the sequence of minimum values
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Add an element to the stack and update the min_stack if necessary.
        """
        self.stack.append(val)
        
        # If the min_stack is empty or the new value is smaller than or equal 
        # to the current minimum, push it onto the min_stack.
        # Note: '<=' is used to handle multiple occurrences of the same minimum value.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove the top element from the primary stack and synchronize min_stack.
        """
        # We must pop the min_stack only if the element being removed from the 
        # primary stack is the current minimum.
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Retrieve the top element of the primary stack.
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element currently in the stack.
        """
        return self.min_stack[-1]

# --- Test Environment ---
if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(f"Current Minimum: {obj.getMin()}") # Expected: -3
    obj.pop()
    print(f"Top Element:     {obj.top()}")    # Expected: 0
    print(f"Current Minimum: {obj.getMin()}") # Expected: -2
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
