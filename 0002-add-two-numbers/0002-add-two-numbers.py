# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        while n1 and n2:
            if not n1.next and n2.next:
                n1.next, n2.next = n2.next, n1.next
            
            _sum = n1.val + n2.val
            cur_val, next_val = _sum % 10, _sum // 10
            if _sum < 10:
                n1.val = _sum
            else:
                n1.val = cur_val
                if n1.next:
                    n1.next.val += next_val
                else:
                    n1.next = ListNode(next_val)
            n1, n2 = n1.next, n2.next
        
        while n1:
            n1.val, next_val = n1.val % 10, n1.val // 10
            if next_val > 0:
                if n1.next:
                    n1.next.val += next_val
                else:
                    n1.next = ListNode(next_val)
            n1 = n1.next
        
        return l1