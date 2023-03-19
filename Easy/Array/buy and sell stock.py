"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in
the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""


# time complexity is 0(n) since this is a two pointer solution scanning array once.
# Space complexity is O(1) since we just used pointers no extra array
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # indices for two pointer buy is left, right is sell
        buy = 0
        sell = 1

        # variable to store current maximum profit
        max_profit = 0

        # while the right pointer is still within array to check
        while sell < len(prices):
            # check if current buy sell values are profitable
            if prices[buy] < prices[sell]:
                # calculate the profit
                curr_profit = prices[sell] - prices[buy]
                # check if we now have a bigger profit and update it
                max_profit = max(max_profit, curr_profit)

            # if it wasn't profitable then the sell value was less, we update buy value to it
            else:
                buy = sell

            # regardless we keep checking rest of array by moving sell pointer
            sell += 1

        # return the maximum profit
        return max_profit



