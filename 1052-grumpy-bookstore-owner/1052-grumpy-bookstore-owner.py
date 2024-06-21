class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        totalSatisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        additionalSatisfied = 0
        currentWindowSatisfied = 0
        
        for i in range(minutes):
            if grumpy[i] == 1:
                currentWindowSatisfied += customers[i]
        additionalSatisfied = currentWindowSatisfied
        for i in range(minutes, n):
            if grumpy[i] == 1:
                currentWindowSatisfied += customers[i]
            if grumpy[i - minutes] == 1:
                currentWindowSatisfied -= customers[i - minutes]
            additionalSatisfied = max(additionalSatisfied, currentWindowSatisfied)
        return totalSatisfied + additionalSatisfied