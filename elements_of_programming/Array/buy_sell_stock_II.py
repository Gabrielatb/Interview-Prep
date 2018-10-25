# Design an algorithm to find the maximum profit. You may complete at most two transactions.


def maxProfit(price):
      
    # Create profit array and initialize it as 0 
    n = len(price)
    profit = [0]* n
      
    # Get the maximum profit with only one transaction 
    # allowed. After this loop, profit[i] contains maximum 
    # profit from price[i..n-1] using at most one trans. 
    max_price=price[n-1] 
      
    for i in range( n-2, 0 ,-1): 
        # print i
          
        if price[i]> max_price: 
            max_price = price[i] 
        # print 'max_price ', max_price
              
        # we can get profit[i] by taking maximum of: 
        # a) previous maximum, i.e., profit[i+1] 
        # b) profit by buying at price[i] and selling at 
        #    max_price 
        print profit[i+1]
        profit[i] = max(profit[i+1], max_price - price[i]) 
    print profit







    # print 'this is the length ', len(prices)
    # first_buysell_profit = [0] * len(prices)

    # min_price_so_far, max_profit = float('inf'), 0
    # for indx, price in enumerate(prices):
    #     max_profit_today = price - min_price_so_far
    #     max_profit = max(max_profit, max_profit_today)
    #     first_buysell_profit[indx] = max_profit
    #     min_price_so_far = min(price, min_price_so_far)
    # # print first_buysell_profit

    # max_price_so_far = float('-inf')
    # for i, price in reversed(list(enumerate(prices[1:],1))):
    #     # print 'this is price ', price, 'this is index ', i
    #     max_price_so_far = max(max_price_so_far, price)
    #     print 'this is max_price_so_far ', max_price_so_far
    # #     print 'this is max_profit ', max_profit, 'this is calc ', max_price_so_far - price + first_buysell_profit[i-1]
    #     max_profit = max(max_profit, max_price_so_far - price + first_buysell_profit[i-1])
    # # # return max_profit


print maxProfit([12, 11, 13, 9, 12, 8, 14, 13, 15])

























# def max_profit(prices):

#     if len(prices) <= 1:
#         return 0

#     curr_max_profit = 0
#     min_price = float('inf')
#     first_buysell_profit = [0] * len(prices)

#     #Each day we are recording the max profit for that day 
#     for i, price in enumerate(prices):
#         if price < min_price:
#             min_price = price
#         elif price - min_price > curr_max_profit:
#             curr_max_profit = price - min_price
#             first_buysell_profit[i] = curr_max_profit

    





