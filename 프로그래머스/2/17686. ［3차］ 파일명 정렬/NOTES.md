NOTE: 정렬 알고리즘 중 안정 정렬을 사용해야하는 문제
**정렬 알고리즘 중 안정정렬에 해당하는 알고리즘은?**

파이썬과 정렬: 내장 정렬 함수의 정렬 알고리즘과 시간복잡도

- sorted: timsort 알고리즘(insert와 merge를 결합한 알고리즘) (nlogn)

참조 지역성

- 최근에 참조한 메모리나 그 인접한 메모리를 다시 참조할 확률이 높다는 원리에 기반하여 캐시 메모리에 저장
- 연속으로 읽는 데이터가 무작위로 읽는 데이터보다 빠르다 (캐시 메모리에서 가져오기 때문)

heap sort, merge sort, quick sort와 참조 지역성

- heap sort < merge sort < quick sort
- 같은 nlogn의 시간복잡도를 갖더라도, 참조 지역성 원리에 따라 세 알고리즘의 상수값이 달라진다
- heap sort: 해당 요소의 인덱스 두 배 또는 절반인 요소 비교 -> 참조 지역성이 좋지 않다
- merge sort: **인접한** 두 덩어리 비교 -> 비교적 참조 지역성이 좋다. 그러나 n의 공간 복잡도
- quick sort: pivot 주변 요소 비교 -> 참조 지역성이 가장 좋다. 그러나 pivot 선정 방식에 따라 시간복잡도 차이가 크게 난다.

- [ ] tim sort

## Reference

- [naver D2 | Tim sort에 대해 알아보자](https://d2.naver.com/helloworld/0315536)
