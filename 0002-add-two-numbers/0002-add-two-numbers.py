# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def up(self, node: ListNode):
        if node.val < 10:
            return
        node.val, next_val = node.val % 10, node.val // 10
        if node.next:
            node.next.val += next_val
        else:
            node.next = ListNode(next_val)
                
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        while n1 and n2:
            if not n1.next and n2.next:
                n1.next, n2.next = n2.next, n1.next
            
            n1.val += n2.val
            self.up(n1)
            n1, n2 = n1.next, n2.next
        
        while n1:
            self.up(n1)
            n1 = n1.next
        
        return l1