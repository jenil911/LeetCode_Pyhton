# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr=head
        matrix=[[-1] * n for _ in range(m)]
        r=0
        c=0
        d_p=0
        d=[(0,1),(1,0),(0,-1),(-1,0)]
        while curr:
            matrix[r][c]=curr.val
            curr=curr.next
            next_r,next_c=r+d[d_p%4][0],c+d[d_p%4][1]
            if 0<=next_r<m and 0<=next_c<n and matrix[next_r][next_c]==-1:
                r,c=next_r,next_c
            else:
                d_p+=1
                r,c=r+d[d_p%4][0],c+d[d_p%4][1]
        return matrix
        