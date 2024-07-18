#code 1
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        MAX_DISTANCE = 10

        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [0] * (MAX_DISTANCE + 1)
            
            if not node.left and not node.right:
                res = [0] * (MAX_DISTANCE + 1)
                res[1] = 1
                return res
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            for i in range(1, distance + 1):
                for j in range(1, distance - i + 1):
                    self.count += left[i] * right[j]
            
            res = [0] * (MAX_DISTANCE + 1)
            for i in range(1, MAX_DISTANCE):
                res[i + 1] = left[i] + right[i]
            
            return res

        dfs(root)
        return self.count