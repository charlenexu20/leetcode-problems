class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Add an extra step with cost 0 to handle reaching the top
        cost.append(0)

        for i in range(len(cost) - 3, - 1, - 1):
            # update the cost of the current step
            cost[i] += min(cost[i + 1], cost[i + 2])

        # Return the minimum cost between the initial two steps
        return min(cost[0], cost[1])
        