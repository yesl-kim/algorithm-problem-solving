접근 방식

- 2 sum을 생각했으나 3 sum과 같이 품. 둘 다 똑같을 것이라고 생각
  x의 조건 (t는 time의 요소)
- time의 요소
- t보다 뒤에 있음
- (x + t) % 60 = 0 -> **(x + t)는 60의 배수**
  - 이 부분이 아쉬움!
  - 이런 사고의 흐름으로 60씩 증가하는 x를 **모두** 구했는데 (ex. t = 30, x = 30, 90, 150, ... 60씩 증가하는 수)
  - 핵심은, t의 짝궁은 30, 90, 150이 됐든 결국 30이라는 것
  - 최종 나머지만 알면 됨! 그게 곧 짝꿍이 되는 수 (x)
  - ex. **(30 % 60) = (90 % 60) = (150 % 60)**

참고 코드

- https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/2141645/Python-Two-Sum-Clean-Code
- https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60
