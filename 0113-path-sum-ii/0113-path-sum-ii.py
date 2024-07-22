# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        if root and root.val == targetSum and (root.left or root.right) and not (root.left and root.right):
            return ans
        def dfs(node, target, arr):
            if not node: return
            
            if target - node.val == 0:
                if not node.left and not node.right:
                    arr.append(node.val)
                    ans.append(arr)
                    return
                
            dfs(node.left, target - node.val, [*arr, node.val])
            dfs(node.right, target - node.val, [*arr, node.val])
        dfs(root, targetSum, [])
        return ans