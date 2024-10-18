class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Extract the elements from the linked list
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next

        # Sort the elements
        elements.sort()

        # Create a new sorted linked list
        sorted_head = ListNode(elements[0])
        current = sorted_head
        for val in elements[1:]:
            current.next = new_node = ListNode(val)
            current = new_node

        return sorted_head