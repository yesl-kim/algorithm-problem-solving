## 10진수 -> 이진수 변환

- `bin(x: number): string`
  ```py
  bin(4) # '0b100'
  ```
- format(x: number, 'b'): string
  ```py
  format(4, 'b') # '100'
  format(4, '#b') # '0b100'
  ```
  - 진수 변환 시 prefix를 무시하고 싶을 때 용이
  - '#'을 붙이면 prefix 붙여서 반환

## Iterable.count(<찾고싶은 문자열>)

- 이터러블 객체에서 사용가능한 메소드
- 찾고 싶은 문자열의 개수 반환
  ```py
  s = '01000101010'
  s.count('1')
  ```

## NOTES

- 문제에서는 '0'과 '1'로만 구성된 문자열이 주어지기 때문에, Counter를 사용하기 보다 count 메소드를 사용하는 게 더 가벼울 것 같다.
- '0'과 '1'의 개수 중 하나만 알면 나머지도 알 수 있다.
- 합을 구하는 로직을 최대한 지연시키고, Recur를 generator 함수로 바꿔본다면?

  - 즉, recur 함수가 `Iterable<<변환 횟수>, <제거된 0의 개수>>` 형태로 반환한다면?
  - [중첩된 리스트를 각 인덱스가 같은 요소끼리 더하려면](https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list) zip을 활용할 수 있다..!

  ```py
  lists_of_lists = [[1, 2, 3], [4, 5, 6]]
  [sum(x) for x in zip(*lists_of_lists)]

      # -> [5, 7, 9]

  ```
