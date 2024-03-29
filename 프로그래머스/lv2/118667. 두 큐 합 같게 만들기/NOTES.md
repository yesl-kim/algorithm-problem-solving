X

> 그리디, 반복 종료 조건을 생각하는 것이 핵심

[2024-01-30] 접근방식

1. 합이 큰 곳에서 pop -> 작은 곳으로 append
2. 합이 같아지면 종료
3. 두 큐를 모두 돌아 제자리로 돌아오면 반복 종료 (2n)
   - 자리만 바뀌고 큐는 같아진 상태

시행착오

- 접근방식은 맞았으나 반복 종료 조건 구현에서 막힘
- 각 큐마다 카운트 변수를 두고 pop할 때마다 해당하는 큐의 카운트 변수를 업데이트하려고 했으나 막힘
- 해설을 보니 꼭 해당하는 큐로 카운트하지 않아도 된다 :0
- 최대 반복 횟수를 2n으로 잡았으나 (자리만 바뀌고 큐는 같아진 상태) 해설에서는 4n으로 계산
- 최대 반복 횟수가 4n 인 것은 이해가 안감 (n = 처음 큐의 길이)

ref

- https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
