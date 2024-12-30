class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        ways = [0] * (high + 1)
        ways[0] = 1
        
        for length in range(high + 1):
            if ways[length] == 0:
                continue
            if length + zero <= high:
                ways[length + zero] = (ways[length + zero] + ways[length]) % MOD
            if length + one <= high:
                ways[length + one] = (ways[length + one] + ways[length]) % MOD
        
        count = 0
        for i in range(low, high + 1):
            count = (count + ways[i]) % MOD
        
        return count