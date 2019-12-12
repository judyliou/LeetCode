def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n <= 2:
            return min(cost)
        for i in range(2, n):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
        return min(cost[n-1], cost[n-2])
