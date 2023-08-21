- 리스트보다 set의 주요연산이 더 효율적이긴 하지만 리스트를 set으로 만들 때 o(n)의 시간복잡도가 든다

리팩토링, 시작하기에 앞서
**로직의 단계를 나누고 단계별로 분리**

- 코드의 의도가 잘 드러나도록 한다.
- 이해하기 쉬워 고치기 쉬워진다. (이점)
- 자료구조 -> 알고리즘 -> 자료구조 -> 알고리즘 식으로 나눠본다. (자료구조 단위로 나눠보는 것도 좋은 방법 -> 어떤 자료구조가 필요한지, 더 효율적일지 고민해본다)

이를 토대로 해당 문제의 단계를 나눠보면,

1. 조건에 맞는 조합 구하기
   - 조건: 나머지 요소(= 두 요소의 합)가 두 요소보다 뒤에 있어야함 (요소의 중복 사용 방지)
   - 자료구조: 딕셔너리 (조건 확인을 위해 `{ v: i }` 형태 필요, o(1) 탐색 시간)
   - 알고리즘: 두 요소의 조합
2. 조합의 중복 제거
   - 자료구조: 셋
   - 알고리즘: 정렬

`after`

```py
def threesum(xs):
    # 1) 조건에 맞는 조합 구하기
    index = defaultdict(int)
    for i, v in enumerate(xs): # o(n)
        index[v] = i

    res = []
    for (i, j) in combinations(range(len(xs)), 2): #o(n^2)
        x, y, z = xs[i], xs[j], -(xs[i] + xs[j])
        if j < index[z]:
            res.append((x, y, z))

    # 2) 조합의 중복 제거
    return set([tuple(sorted(c)) for c in res])
```

- 하지만 마지막 요소의 인덱스만 저장하는 것은 확장성에 좋지 않다
- 문제가 요소의 값이 아니라, 인덱스를 반환하는 거라면? ... 위의 코드는 자잘한 조건이 변경됐을 때 다시 변경해야되는 코드 (자료구조도 알고리즘도)
- => 등장하는 요소의 모든 인덱스를 저장한다면? 요소가 등장한 횟수를 저장한다면? 변경에 더 유연하지 않을까?

---

한단계 더! 리팩토링 과정

1. occasions 자료구조를 만든다면?

   ```py
   def threesum(nums):
    occasions = Counter(nums[2:])

    res = []
    for (i, j) in combinations(range(len(nums)-1), 2): # o(n^2)
        x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
        occasions[x]-=1
        occasions[y]-=1
        if 0 < occasions[z]:
            res.append((x, y, z))
        occasions[x]+=1
        occasions[y]+=1

    return set([tuple(sorted(c)) for c in res])
   ```

   - occasions를 변경하는 것이 찜찜하다 -> 더 좋은 방법은 없을까?
   - `pros`: occasions[x] -= 1 은 '사용한다'라는 의미를 명확하게 표현한다
   - `cons`: occasions[x] += 1 원복을 위한 코드가 꼭 필요하며, 이것이 코드를 지저분하게 한다
   - `alternate`: if int(x == z) + int(y == z) < occasions[z] 라고 표현하면 어떨까
     - `pros`: occasions를 직접 변경하지 않는 장점이 있다
     - `cons`: 하지만 확장성에 좋지 않다. 만일 다른 요구사항이 추가되면? 결국 한 줄로 표현할 수 없다 -> 수정범위가 더 커질 것이다
   - `solution`: '사용 후 원복'하는 코드를 추상화하면 어떨까 -> with 구문 활용

2. with 구문을 활용하여 추상화

   ```py
   class Occtools():
    def __init__(self, arr):
        self.data = Counter(arr)
        self.actions = []

    @property
    def occasions(self):
        return self.data


    def __enter__(self):
        print('enter')
        return self


    def use(self, *keys):
        for key in keys:
            self.data[key] -= 1
            self.actions.append(key)


    def __exit__(self, *args):
            for x in self.actions:
                self.data[x] += 1
            self.actions = []

    def threesum(nums):
        occtools = Occtools(nums[2:])
        occasions = occtools.occasions

        res = []
        for (i, j) in combinations(range(len(nums)-1), 2): # o(n^2)
            with occtools:
                x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
                occtools.use(x, y)
                if 0 < occasions[z]:
                    res.append((x, y, z))

        return set([tuple(sorted(c)) for c in res])

   ```

   - occtools가 너무 많은 일을 한다
   - Occtools의 역할 (occations를 조작하는 함수들의 모음) 때문에 (불필요하게) 클래스가 더 복잡 + 확장될 가능성이 높다

3. Occtools -> Lock

   ```py
   lock = lambda occ: lambda x: Lock(x, occ)

   class Lock():
    def __init__(self, x, occ) -> None:
        self.key = x
        self.occasions = occ

    def __enter__(self):
        self.occasions[self.key] -= 1

    def __exit__(self, *args):
        self.occasions[self.key] += 1


    def threesum(nums):
        occasions = Counter(nums)
        _Lock = lock(occasions)

        res = []
        for (i, j) in combinations(range(len(nums)), 2):
            x, y, z = nums[i], nums[j], -(nums[i] + nums[j])
            with _Lock(x), _Lock(y):
                if 0 < occasions[z]:
                    res.append((x, y, z))

        return set([tuple(sorted(c)) for c in res])
   ```

   - '원복'만이 아니라 '**사용 후 원복**'을 추상화
   - 여기서 필요한 본질은 비교! z를 사용할 수 있는지
   - 비교를 위한 세부 구현 (= 나머지 요소를 사용 후 원복하는) 코드는 Lock으로 추상화 -> 비교하는 코드가 더 깔끔히 드러남!

4. 자질구레한 코드 스멜 제거
   - `occasions = Counter(nums[2:])` -> `occasions = Counter(nums)`
   - `for (i, j) in combinations(range(len(nums)-1), 2)` -> `for (i, j) in combinations(range(len(nums)), 2)`
   - 엄연히 매직넘버는 아니지만 저런 숫자의 사용은 득보다 실이 더 큼
   - `pros`: 순회를 한 두번 덜 할 수 있다
   - `cons`:
     - 이해하기 어렵다 (_'2는 뭐지?'_, _'-1을 왜 했지?'_)
     - 실수하기 쉽다 (_'2했으니까 -2하면 되겠지~'_)
     - 번외) 슬라이싱을 위해 순회를 더 하게 됨 (_장점마저 없어졌지~_)

> \***매직넘버**
>
> - 설명할 수 없는 의미가 있는 고유한 값 또는 명명된 상수로 대체할 수 있는(가급적) 여러 항목
> - 파일 형식 이나 프로토콜을 식별하는 데 사용되는 상수 숫자 또는 텍스트 값입니다 . 파일의 경우 파일 서명 목록을 참조하세요.
> - 다른 의미로 오인될 가능성이 없는 고유한 고유 값(예: Globally Unique Identifiers )
> - 출처: 위키피디아
>
> => 코드를 읽는 사람이 그 의미를 바로 알기 어려운 숫자 (상수)

---

정리!
이전 코드와 비교하여 좋은 점

- 로직의 단계와 의도가 분명히 드러난다 -> 이해하기 쉽다
- 이전 코드는 hash가 무엇을 뜻하는지 알기 어렵다
- 조합의 유효성을 확인하는 코드와 조합의 중복을 피하는 코드가 섞여있어 이해하기 어렵다
