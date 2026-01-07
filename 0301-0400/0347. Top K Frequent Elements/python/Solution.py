from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a frequency map (tallying)
        # We use Counter to build a dictionary where:
        # Key = the number from nums
        # Value = the number of times it appears (frequency)
        # Time Complexity: O(n) as we traverse the list once.
        count = Counter(nums)
        
        # Step 2: Extract the top K frequent elements
        # The most_common(k) method is highly optimized.
        # It internally uses a Heap (Priority Queue) or Sort depending on input size.
        # It returns a list of tuples: [(element1, freq1), (element2, freq2), ...]
        # Time Complexity: O(n log k) because it maintains a heap of size k.
        top_k_tuples = count.most_common(k)
        
        # Step 3: Transform the result using List Comprehension
        # We only need the element (item[0]), not the frequency (item[1]).
        # This creates a list of just the numbers.
        return [item[0] for item in top_k_tuples]

# --- Testing Block ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Multiple elements with varying frequencies
    input1, k1 = [1, 1, 1, 2, 2, 3], 2
    print(f"Test Case 1: Input {input1}, k = {k1}")
    print(f"Result: {sol.topKFrequent(input1, k1)}")
    # Expected: [1, 2]

    # Test Case 2: Single element
    input2, k2 = [1], 1
    print(f"\nTest Case 2: Input {input2}, k = {k2}")
    print(f"Result: {sol.topKFrequent(input2, k2)}")
    # Expected: [1]

    # Test Case 3: More complex frequency distribution
    input3, k3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2
    print(f"\nTest Case 3: Input {input3}, k = {k3}")
    print(f"Result: {sol.topKFrequent(input3, k3)}")
    # Expected: [1, 2]