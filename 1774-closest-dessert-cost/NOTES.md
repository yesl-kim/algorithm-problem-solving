​global과 nonlocal

- global: 전역변수 -> 전역에서 해당 변수를 찾음
- nonlocal: 가장 가까운 상위 스코프에서 해당 변수를 찾음
- global과 nonlocal을 쓰게 되면 외부 변수를 변경한다는 것이므로 좋지 않음 (영향 관계를 파악하기 어려움 -> 유지보수 어려움)
- 반대로 외부에 영향을 주지 않도록 함수 내부에서 지역변수만을 사용 -> 계산 -> 값을 반환하는 형태가 제일 좋음 (순수함수)
- https://stackoverflow.com/questions/71373859/sharing-variables-across-recursion-calls-lists-sets
