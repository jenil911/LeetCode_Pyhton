class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #gas =  [2,3,4]
        #cost = [3,4,3]
        #total =-1,-1,1
        #sum of gas>= sum cost array
        sum_cost = sum(cost)
        sum_gas = sum(gas)
        # Check if it is possible to complete the journey
        if sum_cost > sum_gas:
            return -1

        current_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        return starting_index
        