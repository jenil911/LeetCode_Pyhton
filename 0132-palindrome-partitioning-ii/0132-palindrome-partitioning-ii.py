class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Preprocess the string to determine which substrings are palindromes
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
        
        # Step 2: Use dynamic programming to determine the minimum cuts needed
        cuts = list(range(n))
        for i in range(1, n):
            if dp[0][i]:
                cuts[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        cuts[i] = min(cuts[i], cuts[j]+1)
        
        # Step 3: Return the final answer
        return cuts[-1]