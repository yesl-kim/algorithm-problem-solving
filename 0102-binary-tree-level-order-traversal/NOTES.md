​## [zip_longest 함수: 맵핑하는 요소의 길이가 다를 때 길이가 긴 요소에 맞추고 싶다면](https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length)

1. python@3.x.x
   - itertools.zip_longest
   - fillvalue 속성을 통해 빈 값 처리 지정도 가능!
2. python@2.x.x
   - map 함수 활용, 콜백함수에 None 전달
   - 3버전 이상에서 map은 다르게 동작 (주의)
