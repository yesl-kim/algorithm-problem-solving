## 제출답안

> o(n)

- 새로운 배열 생성, 반환 -> 공간복잡도가 크게 나옴

## 다른 풀이

```py
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        p = intervals[0]
        i = 1
        while i < len(intervals):
            c = intervals[i]
            if c[0] <= p[1]:
                intervals[i-1][1] = max(p[1], c[1])
                del intervals[i]
            else:
                p = c
                i += 1
        return intervals
```

- intervals 배열을 직접 수정
- `del` 키워드로 배열 요소 삭제 가능
