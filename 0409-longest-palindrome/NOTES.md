### best practice

```javascript
var longestPalindrome = function (s) {
  const set = new Set()
  let count = 0

  for (const char of s) {
    if (set.has(char)) {
      count += 2
      set.delete(char)
    } else {
      set.add(char)
    }
  }

  return count + (set.size > 0 ? 1 : 0)
}
```

- 문자열도 for ...of 문으로 바로 순회가 가능하다. 배열로 전환시킬 필요가 없다
- Set 자료구조를 사용한 게 생소
- 순회를 돌면서 바로 길이를 더하는 방식
- 길이수가 짝수(2)가 되면 바로 길이를 더하고, 길이가 홀수인 개수만 남긴다는 점

### Set vs Map

set

- 배열과 비슷하지만, 중복되는 값이 없다는 것이 특징

Map

- 키와 값으로 이루어졌다는 점에서 객체와 유사
