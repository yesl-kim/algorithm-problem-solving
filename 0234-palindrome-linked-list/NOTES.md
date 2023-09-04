2023.09.04 월
제출 풀이: list 변환 후 투 포인터 활용 (o(n + n/2) => o(n))

다른 풀이: runner 활용 (`0234-palindrome-linked-list modified`)

- 리스트 변환없이 한 번의 순회로 풀 수 있다.
- fast runner, slow runner -> slow 보다 2배 빠른 fast runner
- fast가 도착할 쯤 slow는 정확히 연결리스트의 중간에 오게됨
- slow는 중간까지는 연결리스트의 값을 저장, 중간 이후부터는 저장한 값과 비교

그런데 runner를 활용한 풀이보다 첫 풀이가 더 직관적이어서 좋은 것 같다.
효율 대비 가독성이 첫 풀이가 더 좋지 않나- 하는 생각이 든다.
