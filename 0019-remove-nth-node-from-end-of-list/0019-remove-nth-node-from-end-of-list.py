# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = {}
        node = head
        label = 0
        while node:
            nodes[label] = node
            label += 1
            node = node.next
        nth = label-n
        if nth == 0:
            return nodes[nth].next
        else:
            nodes[nth-1].next = nodes[nth].next
            return head
        