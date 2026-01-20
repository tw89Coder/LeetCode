from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Main Idea:
        We maintain a 'min_price' to track the best day to buy so far, 
        and a 'max_profit' to record the maximum difference we've seen.
        By iterating once, we ensure O(n) efficiency.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        # Initialize min_price to infinity to ensure the first price becomes the min.
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest purchase price found so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if we sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

# --- Educational Test Suite ---
if __name__ == "__main__":
    sol = Solution()
    test_prices = [7, 1, 5, 3, 6, 4]
    # Trace:
    # 7: min=7, profit=0
    # 1: min=1, profit=0
    # 5: min=1, profit=max(0, 5-1)=4
    # 6: min=1, profit=max(4, 6-1)=5
    print(f"Maximum Profit: {sol.maxProfit(test_prices)}") # Output: 5