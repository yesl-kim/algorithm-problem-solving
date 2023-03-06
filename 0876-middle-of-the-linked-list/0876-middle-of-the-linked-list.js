/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const middleNode = (head) => {
  if(!head.next) return head
  
  let next = head
  let i = 1
  let middle
  
  while(next.next) {
    i++
    next = next.next
  }
  
  middle = Math.floor(i/2)
  next = head
  i = 0
  
  while(i < middle) {
    next = next.next
    i++
  }
  return next
}