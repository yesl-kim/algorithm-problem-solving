## 풀이 과정

### #1. 시퀀스의 길이를 나타내는 length 자료구조 (해시맵) -> `오답`

접근방식

- 시퀀스: 앞, 뒤 요소에 연결가능
- 구하는 것은 길이 -> 길이를 저장하자!
- 해시맵 length[x]는 x가 포함된 시퀀스의 **길이**
- `length[x] = length[x-1] + length[x+1] + 1`
- nums를 순회하며 위의 식을 적용 -> length 값 중 최대값 반환

예외 케이스

- input: [3,2,4]
- length: [1,2,2]
- 기대되는 length: [1,2,3]
- 시퀀스가 달라질 때마다 length[x]만 수정하고 있기 때문에 오답
  - 시퀀스가 달라질 때마다 (=시퀀스의 길이가 달라질 때마다) 시퀀스에 속한 **모든 요소에 대하여** 길이가 수정되어야함
  - 재귀적으로....?
  - tip: 양 끝만

### #2. 시퀀스가 달라질 때마다 시퀀스 양 끝 점의 길이 계산 다시 -> `오답`

```py
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = defaultdict(int)
        res = 0
        for x in nums:
            left, right = length[x-1], length[x+1]
            _len = left + right + 1
            length[x - left] = length[x + right] = _len
            res = max(res, _len)

        return res
```

접근방식

- [x - length[x-1]] = 앞 시퀀스의 시작점
- [x + length[x+1]] = 뒤 시퀀스의 끝 점
- length[시작점] = length[끝점] = 새로운 길이

예외 케이스

- input: [1,2,0,1]
- output: 7
- expected: 3
- 이미 기존 시퀀스에 연결된, 시퀀스 중간에 속해있는 요소에 오답
- 속해있는 경우 길이를 다시 계산하면 안됨
  - 속해있는 경우 = 이미 방문한 경우 건너뜀
  - 방문 검사 필요? 아니면 속함 여부?
  - tip: 자료구조가 잘못되었다. 정보가 너무 부족

다시 생각해보자: 어떤 자료구조가 필요한가

- x가 속하는 시퀀스의 길이
- 속한 시퀀스: 속한 시퀀스를 알면 그 길이를 알 수 있음
- 시퀀스의 양 끝 점: 양 끝 점을 알면 시퀀스를 알 수 있음
- 자료구조: `sequences = {[num]: (start, end)}`

### #3. 자료구조 변경: 시퀀스의 양 끝 점을 나타내는 sequences -> `오답`

```py
class Solution:
    def length(self, sequence):
        return sequence[1] - sequence[0] + 1

    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}
        for x in nums:
            start = sequences.get(x-1, (x, None))[0]
            end = sequences.get(x+1, (None, x))[1]
            sequences[start] = sequences[end] = (start, end) # 새로운 시퀀스의 시작점, 끝 점에 해당하는 시퀀스만 다시 수정

        if not sequences:
            return 0
        return self.length(max(sequences.values(), key=self.length))
```

접근방식

- 초반과 동일
- 범위 수정 -> 속함 여부에 따라 변경여부를 달리할 필요없음
- 앞 시퀀스의 시작점 ~ 뒤 시퀀스의 끝 점 연결 -> 새로운 시퀀스!
- 새로운 시퀀스 시작점, 끝 점에 해당하는 sequences만 수정!

오류 케이스

- 초반과 동일하게 이미 계산한 요소 + 시퀀스 중간에 있는 요소 (중복요소)를 다시 계산하게 될 때 문제 발생 (덮어쓰는 문제)
- input: [-1,9,-3,-6,7,-8,-6,2,9,2,3,-2,4,-1,0,6,1,-9,6,8,6,5,2]
- 시퀀스를 연결하는데는 요소 하나면 충분. 같은 요소가 여러개 있을 필요 없음 (사실 여러개 있어서 더 방해됨)
- set 자료구조 활용 (o(n)이니까 문제 요구사항에도 벗어나지 않음)

### #4. set 자료구조 활용하여 중복 요소 제거 -> `정답` (`o(3n)`)

- 간단히 nums를 set으로 변환 -> 중복 요소 제거한 것으로 해결

### #번외. 시간복잡도를 좀 더 최적화시켜보자 (3n -> 2n으로 줄여보자)

접근방식

- 간단히 sequences에 현재 요소가 이미 있는지 확인 -> 있으면 continue
- -> set 자료구조를 사용하지 않고 중복 요소 방지하기

오답: 구현실수 ~~정말 실수일까?~~

- 방문 검사하면서 sequences[x]에 값을 넣어주지 않음,, 시작점, 끝점만 넣어줌 -> 시간 굉장히 많이 소요

문제: 수정했으나 기존 보다 (set을 활용했을 때보다) 더 빠르지 않음;;

- 원인은 최종값(시퀀스의 길이)를 계산하는 부분이 아니었을까..
- 어디서 비효율이 발생하는지 잘못 짚음
