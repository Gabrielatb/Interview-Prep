# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.


# Input: [7,1,5,3,6,4]

#4, [7,1,5,3,6]



# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    
    #[7,6(i),4,3,1]
    # max_proft = -1
    
# time complexity O(n**2)
# space complexity O(1)
    maxprofit = 0
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maxprofit:
                maxprofit = profit
    return maxprofit

############################################
#Time Complexity O(n)
#Space Complexity O(1)
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price_so_far, max_profit = float('inf'), 0
    for price in prices:
        max_profit_sell_today = price- min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit

