class Solution:
    def strangePrinter(self, s: str) -> int:
        return (f:=cache(lambda i,j:i<=j and min([1+f(i+1,j)]+[f(i,k-1)+f(k+1,j) for k in range(i+1,j+1) if s[k]==s[i]])))(0,len(s:=''.join(c for c,_ in groupby(s)))-1)