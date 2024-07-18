# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def middle(curr = None):
            if curr:
                prev = slow = fast = curr
                while fast and fast.next:
                    prev = slow
                    slow = slow.next
                    fast = fast.next.next
                return prev
        def helper(curr=None):
            if curr:
                pre_mid = middle(curr)
                if not pre_mid.next:
                    return TreeNode(pre_mid.val)
                parent = pre_mid.next
                pre_mid.next = None
                root = TreeNode(parent.val)
                root.right = helper(parent.next) 
                root.left = helper(curr)
                return root
        return helper(head)