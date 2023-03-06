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
const reverseList = (head) => {
  if(!head || !head.next) return head
  
  let cur = head
  let prev = null
  
  while(cur) {
    const temp = cur.next
    cur.next = prev
    prev = cur
    cur = temp
  }
  
  return prev
}