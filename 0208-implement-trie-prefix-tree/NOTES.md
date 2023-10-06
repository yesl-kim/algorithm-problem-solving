## 리팩토링

### 1. 반복되는 로직 분리

- 주어진 word가 트리에 있는지 확인하는 로직
- 예외 처리를 통해 word가 트리에 있는지 없는지 구분할 수 있음

알게된 것

- 예외처리시 값 throw 하기

  ```py
  ...
  raise Exception(a, b, ...) # 여러 값을 throw 할 수 있음

  ...
  try:
    ...
  except Exception as error:
    a, b = error.args # 값은 args 프로퍼티에 담기고, 이를 unpack할 수 있음
  ```
