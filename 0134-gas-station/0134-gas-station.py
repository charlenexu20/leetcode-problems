class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy | tc: O(N) | sc: O(1)

        # Check if total gas is less than total cost
        if sum(gas) < sum(cost):
            return -1
        
        total = 0 # current gas balance
        start_idx = 0 # starting index for the potential circuit

        for i in range(len(gas)):
            # Calculate net gas at the current station
            total += (gas[i] - cost[i])

            # If total gas balance drops below zero,
            # it means we cannot start from 'start_idx' to 'i'
            if total < 0:
                total = 0
                start_idx = i + 1
            
        return start_idx
            

        