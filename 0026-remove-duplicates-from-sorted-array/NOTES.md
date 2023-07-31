## 제출답안

> 0(n)

- 중복되지 않는, 최신값을 저장 (val) 현재요소를 val과 비교하며 중복 요소 제거

## 모범답안

> 0(n)

```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
```

- 바로 이전요소와 값을 비교 -> 최신값 저장할 필요 x
