2024-04-28

- **하나 이상**의 공백문자로 구분될 수 있기 때문에 단어를 나눌 때 `split()`이 아닌 `split(" ")`로 명시해주어야함
- 처음 시도한 아래 코드보다 split 이후 각 단어를 치환하는 코드가 더 선언적이어서 좋은 코드같다

  ```py
  def solution(s):
  i = 0
  ns = ''
  for char in s:
      if char == ' ':
          i = 0
          ns += char
          continue

      if i % 2 == 0:
          ns += char.upper()
      else:
          ns += char.lower()
      i += 1
  return ns
  ```
