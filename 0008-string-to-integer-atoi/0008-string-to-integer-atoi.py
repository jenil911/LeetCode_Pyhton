class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        res = 0
        dig = False
        posi = False
        neg = False
        other = False
        
        i = 0
        while i < n and s[i] == ' ':
            i += 1
            
        for j in range(i, n):
            if other:
                break
                
            if '0' <= s[j] <= '9':
                res = (res * 10) + (ord(s[j]) - ord('0'))
                dig = True
            else:
                if dig:
                    break
                
                elif s[j] == '-' and not neg:
                    neg = True
                    
                elif s[j] == '+' and not posi:
                    posi = True
                    
                else:
                    other = True
                    
        if posi and neg:
            return 0
        
        if neg:
            res = -res
            
        if res > 2**31 - 1:
            return 2**31 - 1
        
        if res < -2**31:
            return -2**31
        
        return int(res)