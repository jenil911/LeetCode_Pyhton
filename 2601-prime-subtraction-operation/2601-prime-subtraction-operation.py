import math

class Solution:
    # Checks if a number is prime
    def isPrime(self, number: int) -> bool:
        if number < 2:
            return False
        
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Process each number in the array
        for i in range(len(nums)):
            # Calculate the upper bound for subtraction
            bound = nums[0] if i == 0 else nums[i] - nums[i - 1]
            
            # If bound is not positive, sequence is impossible
            if bound <= 0:
                return False
            
            # Find the largest prime number less than bound
            largestPrime = 0
            for j in range(bound - 1, 1, -1):
                if self.isPrime(j):
                    largestPrime = j
                    break
            
            # Subtract the largest prime from current number
            nums[i] -= largestPrime
        
        return True