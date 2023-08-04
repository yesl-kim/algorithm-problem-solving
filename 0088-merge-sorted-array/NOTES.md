​접근방식

- 병합정렬 사용
- nums1을 직접 변경하기 위해 공간 필요 -> nums1을 앞에 n만큼의 공간이 있는 형태로 변경 (뒤로 싹 밀기)
- ex. [1,2,3,0,0,0], m=3 -> [0,0,0,1,2,3]
- 그 뒤로 nums1에 바로 병합정렬 (two pointers)
- nums1의 앞에서부터 작은 숫자를 insert

비슷한 다른 풀이

```py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m+n-1
        n1 = m-1
        n2 = n-1

        while n1 >= 0 and n2 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[last] = nums1[n1]
                n1 -= 1
            else:
                nums1[last] = nums2[n2]
                n2 -= 1
            last -= 1

        while n2 >= 0:
            nums1[last] = nums2[n2]
            n2 -= 1
            last -= 1
```

- 뒤에 공간이 있기 때문에 뒤에서부터 큰 숫자를 insert
- => nums1을 뒤로 밀어줄 필요 없음
