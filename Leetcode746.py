# this code is used to answer the leetcode No. 746
test_case = {15: [10, 15, 20], 6: [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]}


class solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        init = 0
        dp = [0] * length
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, length):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])


s = solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
