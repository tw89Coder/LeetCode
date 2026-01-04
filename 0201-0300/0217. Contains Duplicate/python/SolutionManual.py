# The manual loop version (Early exit)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if any value appears at least twice in the array.
        Approach: Hash Set for O(n) average time complexity.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Unit Testing for Verification
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        {"input": [1, 2, 3, 1], "expected": True},
        {"input": [1, 2, 3, 4], "expected": False},
        {"input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], "expected": True}
    ]
    
    for i, test in enumerate(test_cases):
        result = sol.containsDuplicate(test["input"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test Case {i+1}: {status} (Input: {test['input']}, Result: {result})")
        
        from typing import List