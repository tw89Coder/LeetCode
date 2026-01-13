from typing import List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Main Idea:
        Instead of a standard O(n^2) Two-Pointer scan, we partition the numbers by sign 
        (Negative, Zero, Positive) and use Frequency Mapping to solve the problem as a 
        constrained combination puzzle. This bypasses slow Python loops and leverages 
        C-optimized hash lookups.
        
        Complexity:
            Time: O(n^2) - Average performance is much faster due to unique-element iteration.
            Space: O(n) - For storing frequencies and partitioned sets.
        """
        res = set() # Use a set to automatically handle duplicate triplets
        
        # 1. Frequency count and partitioning
        # Separating numbers into groups reduces the search space by eliminating
        # impossible combinations (e.g., three positives cannot sum to zero).
        n_count = Counter(nums)
        negatives = sorted([n for n in n_count if n < 0])
        positives = sorted([p for p in n_count if p > 0])
        zeros = n_count.get(0, 0)

        # CASE 1: Triple Zero [0, 0, 0]
        if zeros >= 3:
            res.add((0, 0, 0))

        # CASE 2: Single Zero Pivot [negative, 0, positive]
        # For every negative 'n', check if its positive counterpart '-n' exists.
        if zeros >= 1:
            for n in negatives:
                if -n in n_count:
                    res.add((n, 0, -n))

        # CASE 3: Two Negatives and One Positive [n1, n2, -(n1+n2)]
        # Iterate through pairs of unique negative numbers.
        for i, n1 in enumerate(negatives):
            for n2 in negatives[i:]:
                # If n1 == n2, we need at least two of that negative number.
                if n1 == n2 and n_count[n1] < 2:
                    continue
                
                target = -(n1 + n2)
                # Check if the complement exists in the positive set.
                if target in n_count and target > 0:
                    res.add(tuple(sorted((n1, n2, target))))

        # CASE 4: Two Positives and One Negative [p1, p2, -(p1+p2)]
        # Iterate through pairs of unique positive numbers.
        for i, p1 in enumerate(positives):
            for p2 in positives[i:]:
                if p1 == p2 and n_count[p1] < 2:
                    continue
                
                target = -(p1 + p2)
                # Check if the complement exists in the negative set.
                if target in n_count and target < 0:
                    res.add(tuple(sorted((p1, p2, target))))

        # Final conversion back to list of lists.
        return [list(t) for t in res]

# --- Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    test_nums = [-1, 0, 1, 2, -1, -4]
    # Expected Output: [[-1, -1, 2], [-1, 0, 1]]
    print(f"Input: {test_nums} | Triplets: {sol.threeSum(test_nums)}")