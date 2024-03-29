피드백

1.  **이번 문제에서는 global, nonlocal을 쓰지 않고 global, nonlocal 사용은 좋지 않다. 왜 그럴까?**

    - global: 전역변수 -> 전역에서 해당 변수를 찾음
    - nonlocal: 가장 가까운 상위 스코프에서 해당 변수를 찾음
    - global과 nonlocal을 쓰게 되면 외부 변수를 변경한다는 것이므로 좋지 않음 (영향 관계를 파악하기 어려움 -> 유지보수 어려움)
    - 반대로 외부에 영향을 주지 않도록 함수 내부에서 지역변수만을 사용 -> 계산 -> 값을 반환하는 형태가 제일 좋음 (순수함수)

2.  순수함수의 이름은 형용사(?)로 짓는 것이 자연스럽다 (ex. min, closer, ...)

3.  **처음 calculate 함수는 완전히 분리되지 않았다**

        - 조합하는 함수 calculate 안에서 비교하여 하나의 값을 리턴하도록 closer 함수를 호출하고 있기 때문에
        - calculate 안에서 조합과 비교를 같이 한다.

    **`solution`**: calculate에서는 조합만, closer는 비교만
    => calculate 함수에서는 조합한 금액의 총액의 리스트를 반환한다

    **`problem`**: 이럴 경우 메모리를 너무 크게 차지 (공간 복잡도가 o(3^n))
    => 제너레이터 활용!
    => 제너레이터가 어렵다면, 제너레이터를 반환하는 내장 함수를 활용하는 것도 방법 (`product`)

4.  **의미없는 변수명을 쓸 바엔 람다함수로 만들자**

    ```py
    def closestCost2(baseCosts, toppingCosts, target):

    def closer(a, b):
            abs_a, abs_b = abs(target-a), abs(target-b)
            if abs_a == abs_b:
                return min(a, b)
            else:
                val = {
                    abs_a: a,
                    abs_b: b
                }
                return val[min(abs_a, abs_b)]

    def calculate(total, cb):
        idx, count = cb
        return total + toppingCosts[idx] * count

    res = float('inf')
    for bc in baseCosts:
        for cb in product(range(3), repeat=len(toppingCosts)):
            cost = reduce(calculate, enumerate(cb), bc)
            res = closer(res, cost)

    return res
    ```

    - calculate 는 이 함수 전체에 대한 의미이기도 하니, 의미없는 변수와 같다 (closestCost2 자체가 cost를 계산하는 것이니)
    - 이런 함수는 차라리 람다로 만들어 의미없는 변수명 사용을 줄이자

5.  별로인 트릭
    ```py
    def closer(a, b):
             abs_a, abs_b = abs(target-a), abs(target-b)
             if abs_a == abs_b:
                 return min(a, b)
             else:
                 val = {
                     abs_a: a,
                     abs_b: b
                 }
                 return val[min(abs_a, abs_b)]
    ```
    - 직관적이지도, 코드가 전보다 짧아서 효율이 좋지도 않아서?

---

참고

- [global, nonlocal이 안좋은가](https://stackoverflow.com/questions/71373859/sharing-variables-across-recursion-calls-lists-setss)
- [product 참고](https://stackstackstack.tistory.com/entry/python-순열-조합-함수-product-permutations-combinations)
