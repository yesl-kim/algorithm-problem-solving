​## 시행착오

1. 문제를 잘못 이해

```py
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right=0, x
        res=0
        while left<=right:
            root=(left+right)//2
            if abs(root**2-x) < abs((root+1)**2-x):
                res=root
                right=root-1
            else:
                left=root+1
        return res
```

- 제곱근에 가장 가까운 수 중 **반올림**하는 것으로 착각 (내림!)
- 현재 요소와 다음 요소의 제곱 -> x와의 거리 비교

2. 문제 해석 오류

- _제곱근이 x에 가장 가까운 수 중 작은수를 반환_ 하는 것으로 해석
- 현재 요소의 제곱, 다음 요소의 제곱 -> 두 수중 x와의 거리를 비교하여 범위 좁히기
- 두 수 중 작은 수는 `left` => 자꾸 `left`를 리턴하려고 함

=> `제곱해서 x를 넘지 않는 수 중 최대값을 반환`하는 문제! (통과)
