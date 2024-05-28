class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(map(str,list(permutations(range(1,n+1)))[k-1])) 