/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let node = head
  
  if(!node) {
    return null
  }
  
  while (!node.c) {
    node.c = true
    node = node.next
    
    if(!node) return null
  }
  return node
};