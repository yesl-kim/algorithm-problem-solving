class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head 
        
        next = head.next
        head.next, next.next = next.next, head
        head.next = self.swapPairs(head.next)
        return next