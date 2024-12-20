# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        rev=False
        while q:
            qz=len(q)
            arr=[]
            for i in range(qz):
                Node=q.popleft()
                if Node.left: q.append(Node.left)
                if Node.right: q.append(Node.right)
                if rev:
                    arr.append(Node)
                    if i>=qz/2:
                        arr[i].val, arr[qz-1-i].val=arr[qz-1-i].val, arr[i].val
            rev=not rev
        return root
        