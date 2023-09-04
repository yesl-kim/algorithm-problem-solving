from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        fast = slow = head
        half = []
        while fast and fast.next:
            half.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != half.pop():
                return False
            slow = slow.next
        
        return True
        