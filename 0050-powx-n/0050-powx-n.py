class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n, p):
            if p==0 or n==1: return 1
            if p<0: return 1/helper(n, -p)
            rs = helper(n*n, p//2)
            return rs * n if p&1 else rs
        return helper(x, n)
        
        
            
            
        
                