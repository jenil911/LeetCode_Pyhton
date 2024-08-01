class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The variables are long for better understanding
        
        # Initialize variables to track minimum prices and maximum profits
        min_price_after_first_buy = float('inf')
        max_profit_after_first_sell = 0
        min_price_after_second_buy = float('inf')
        max_profit_after_second_sell = 0
        
        for price in prices:
            # Update the minimum price for the first buy
            min_price_after_first_buy = min(min_price_after_first_buy, price)
            
            # Calculate profit after the first sell
            max_profit_after_first_sell = max(max_profit_after_first_sell, price - min_price_after_first_buy)
            
            # Update the minimum price for the second buy
            min_price_after_second_buy = min(min_price_after_second_buy, price - max_profit_after_first_sell)
            
            # Calculate profit after the second sell
            max_profit_after_second_sell = max(max_profit_after_second_sell, price - min_price_after_second_buy)
        
        return max_profit_after_second_sell