from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def find_nth_next(node, n):
            if not n:
                return node
            return find_nth_next(node.next, n - 1)
        
        prev = None
        cur = head
        nth_next = find_nth_next(head, n)
        while nth_next:
            prev = cur
            cur = cur.next
            nth_next = nth_next.next
        
        if not prev:
            return cur.next
        
        prev.next = cur.next
        return head
        

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode(1, ListNode(2))
head = ListNode(1)
node = Solution().removeNthFromEnd(head, 1)
while node:
    print(node.val)
    node = node.next
print(node)