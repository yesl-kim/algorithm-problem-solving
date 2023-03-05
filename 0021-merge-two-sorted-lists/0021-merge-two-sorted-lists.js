/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */

const recursion = (prev, next) => {
  if(!prev || !next) return
  
  if(!prev.next) {
    prev.next = next
    return
  }
  
  if (prev.next.val < next.val) {
    recursion(prev.next, next)
  } else {
    const _next = next.next
    next.next = prev.next
    prev.next = next
    recursion(prev.next, _next)
  }
}

const mergeTwoLists = (list1, list2) => {
  // 두 리스트 중 하나라도 빈 값인 경우 => 값이 있는 리스트를 반환
   if(!list1 || !list2) return list1 || list2
  
  // 그 외엔 값을 비교
  let merged = null
  let next = null
  if(list1.val < list2.val) {
    merged = list1
    next = list2
  } else {
    merged = list2
    next = list1
  }
  
  recursion(merged, next)
  return merged
}