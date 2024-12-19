class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt=diff=0
        for i, x in enumerate(arr):
            diff+=x-i
            cnt+=(diff==0)
        return cnt
        