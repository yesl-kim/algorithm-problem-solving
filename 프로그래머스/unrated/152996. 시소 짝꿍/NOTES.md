풀이 과정

1. 완전탐색

   1. 짝꿍 조합 (`combinations`)
   2. 유효한 짝꿍인지 확인 (`permutations((2,3,4), 2)` 비율에 속하는지) -> 카운팅
      => **시간초과** `o(m * n^2)` -> `o(n^2)`

2. x가 정해지면 짝꿍 y를 구할 수 있음 `o(n)` + occurrences 활용

   1. occurrences 생성
   2. x를 통해 y 계산
   3. y가 occurrences에 있으면 카운팅
      => 중복 발생 ((a, b) = (b, a))으로 인한 **오답**
      => y 계산 시 permutations가 아닌 combinations로 변경 -> 1:1 비율일 때 동일하게 중복 발생
      => **제한시간 초과**

3. indices 활용
   1. indices 생성
   2. x -> y 계산
   3. **x 요소 뒤에** y 요소의 개수만큼 카운팅 (이진탐색)
      => 이진탐색으로 구현하는 과정에서 조건 실수로 인한 **오답** -> 원인을 찾느라 시간이 꽤 소요
      => **통과**

알게된 것

- 이진탐색 모듈, `bisect` -> `bisect_right` 메소드 활용
