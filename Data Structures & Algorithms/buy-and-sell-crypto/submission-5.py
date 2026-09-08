class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProfit = 0
        for index, item in enumerate(prices):
            if index + 1 != len(prices):
                remArray = prices[index+1:]
                largeNum = max(remArray)
                if largeNum - item > highestProfit:
                    highestProfit = largeNum - item
                else:
                    continue
            else:
                continue
        return highestProfit

        