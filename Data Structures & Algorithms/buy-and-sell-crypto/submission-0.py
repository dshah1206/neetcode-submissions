class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T.C: O(N^2), S.C: O(1) - Brute Force Approach
        """
        # n = len(prices)
        # maxprofit = 0

        # for i in range(n):
        #     buy = prices[i]
        #     for j in range(i+1,n):
        #         sell = prices[j]
        #         maxprofit = max(maxprofit, sell-buy)
        # return maxprofit
        
        """
        T.C: O(N), S.C: O(1) - Two pointer Approach
        """
        buy = 0
        sell = 1
        maxprofit = 0
        n = len(prices)

        while sell < n:
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprofit = max(maxprofit, profit)
            else:
                buy = sell
            sell += 1
        return maxprofit


