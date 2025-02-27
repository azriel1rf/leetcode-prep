class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        previous = None
        current = head
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
