class Solution:
    def minimizedMaximum(self, n: int, q: List[int]) -> int:
        return bisect_left(range(1,max(q)),1,key=lambda x:sum(ceil(v/x) for v in q)<=n)+1