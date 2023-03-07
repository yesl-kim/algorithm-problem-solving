### best practice

```javascript
const detectCycle = (head) => {
  let current = head
  while (current !== null) {
    if (current.visited) return current
    current.visited = true
    current = current.next
  }
  return null
}
```

나의 코드와 다른 점

- while의 조건문
  현재 node가 null인지를 while문 안에서 감지
  나의 코드보다 조건문의 개수가 줄었다. 속도, 메모리도 더 좋았다

```javascript
const detectCycle = (head) => {
  let node = head

  while (node) {
    if (node.visited) {
      delete node.visited
      return node
    } else {
      node.visited = true
      node = node.next
    }
  }

  return null
}
```

- node를 반환하기 전에 추가한 필드를 지운 뒤 반환하는 코드도 있었다.
- 생각하지 못한 부분이지만 위의 코드보다 메모리 사용량이 조금 더 컸다. (속도는 비슷)
