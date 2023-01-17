## 파이썬의 enumerate() 내장 함수로 for 루프 돌리기

<iframe src="https://www.youtube.com/embed/NGby_N-WzAw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

많은 프로그래밍 언어들에서 `i`, `j`, `k`와 같은 소위 인덱스(index) 변수를 증가시키면서 `for` 루프를 돌립니다. 하지만 파이썬에서는 대신 `enumerate()`라는 내장 함수 이러한 인덱스 변수 없이 다소 독특한 방식으로 루프를 돌리는데요.

이번 포스팅에서는 이 부분에 대해서 한 번 알아보도록 하겠습니다.

먼저 파이썬에서 `for` 문을 사용해서 루프를 돌리는 가장 기본적인 방법부터 짚고 넘어가겠습니다.

파이썬에서는 `for` 루프는 기본적으로 `for <원소> in <목록>:` 형태로 작성이 되는데요. 여기서 `<목록>` 부분에는 리스트(list), 튜플(tuple), 문자열(string), 반복자(iterator), 제너레이터(generator) 등 순회가 가능한 왠만한 모든 데이터 타입을 사용할 수 있습니다. `<원소>` 부분은 흔히 순회 변수(loop variable)라고 하는데, `<목록>` 부분에 넘긴 객체가 담고 있는 원소들이 루프가 도는 동안 하나씩 차례로 할당됩니다.

예를 들어, 3개의 글자를 담고 있는 리스트를 대상으로 루프를 돌면서 각 글자를 출력하는 코드를 `for` 문으로 작성해보겠습니다.

```python
>>> for letter in ['A', 'B', 'C']:
...     print(letter)
...
A
B
C
```

여기서 원소 뿐만 아니라 인덱스(index)도 함께 출력하고 싶을 때는 어떻게 해야할까요? 이 부분은 다른 프로그래밍 언어를 사용하시다가 파이썬으로 넘어오신 분들이 처음에 흔히 하는 질문이기도 한데요.

이러한 분들이 흔히 아래와 같은 코드를 작성하는 것을 종종 보게 됩니다.

```python
>>> i = 0
>>> for letter in ['A', 'B', 'C']:
...     print(i, letter)
...     i += 1
...
0 A
1 B
2 C
```

이 방법이 틀린 것은 아니지만, `i` 변수가 for 반복문이 종료된 이 후에도 네임 스페이스에 남아있기 때문에 이상적이지는 않습니다.

또 다른 방법으로는 `range()`와 `len()` 내장 함수를 이용하여 만든 인덱스 목록을 대상으로 루프를 돌리는 것입니다.

```python
>>> letters = ['A', 'B', 'C']
>>> for i in range(len(letters)):
...     letter = letters[i]
...     print(i, letter)
...
0 A
1 B
2 C
```

이 방법은 이전 방법보다는 나아보이지만, 파이썬 커뮤니티에서는 이러한 코드를 소위 파이썬 답지(Pythonic) 않아 보인다고 합니다.

> 파이썬의 `range()` 내장 함수에 대해서는 [별도의 포스팅](https://www.daleseo.com/python-range/)에서 자세히 다루었으니 참고 바랍니다.

## enumerate() 함수

그럼 어떻게 해야 좀 더 파이썬답게 인덱스(index)와 원소를 동시에 접근하면서 루프를 돌릴 수가 있을까요? 🐍

바로 파이썬의 내장 함수인 `enumerate()`를 이용하면 되는데요. `for` 문의 `in` 뒷 부분을 `enumerate()` 함수로 한 번 감싸주기만 하면 됩니다.

```python
>>> for entry in enumerate(['A', 'B', 'C']):
...     print(entry)
...
(0, 'A')
(1, 'B')
(2, 'C')
```

`enumerate()` 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줍니다. 따라서 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기(unpacking)를 해줘야 합니다.

```python
>>> for i, letter in enumerate(['A', 'B', 'C']):
...     print(i, letter)
...
0 A
1 B
2 C
```

## 시작 인덱스 변경

루프를 돌리다보면 인덱스를 0이 아니라, 1로 시작하고 싶을 때가 있습니다. 이럴 때는 `enumerate()` 함수를 호출할 때 `start` 인자에 시작하고 싶은 숫자를 넘기면 됩니다.

```python
>>> for i, letter in enumerate(['A', 'B', 'C'], start=1):
...     print(i, letter)
...
1 A
2 B
3 C
```

```python
>>> for i, letter in enumerate(['A', 'B', 'C'], start=101):
...     print(i, letter)
...
101 A
102 B
103 C
```

## enumerate() 원리

지금까지 `for` 문에서 `enumerate()` 함수를 사용하는 방법에 대해서 알아봤는데요. `enumerate()` 함수 자체가 어떻게 작동하는지 좀 더 살펴보겠습니다.

파이썬에서 `for` 문은 내부적으로 `in` 뒤에 오는 목록을 대상으로 계속해서 `next()` 함수를 호출하고 있다고 생각할 수 있습니다. 따라서, 일반 리스트를 `iter()` 함수에 넘겨 반복자(iterator)로 만든 후 `next()` 함수를 호출해보면 원소들이 차례로 얻어지는 것을 알 수 있습니다.

```python
>>> iter_letters = iter(['A', 'B', 'C'])
>>> next(iter_letters)
'A'
>>> next(iter_letters)
'B'
>>> next(iter_letters)
'C'
```

이 번에는 `enumerate()` 함수를 호출한 결과를 대상으로 `next()` 함수를 계속해서 호출해보면, 인덱스와 원소의 쌍이 튜플(tuple)의 형태로 차례로 얻어지는 것을 알 수 있습니다.

```python
>>> enumerate_letters = enumerate(['A', 'B', 'C'])
>>> next(enumerate_letters)
(0, 'A')
>>> next(enumerate_letters)
(1, 'B')
>>> next(enumerate_letters)
(2, 'C')
```

결국, `enumerate()` 함수는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게 해주는 반복자(iterator) 객체를 반환해주는 함수입니다. 이 부분은 `enumerate()` 함수의 반환 값을 리스트로 변환해보면 좀 더 명확하게 확인할 수 있습니다.

```python
>>> list(enumerate(['A', 'B', 'C']))
[(0, 'A'), (1, 'B'), (2, 'C')]
```

## \[팁\] 2차원 리스트 루프

이제 `enumerate()` 함수의 작동 원리까지 배웠으니 좀 더 고급 응용 사례를 살펴볼까요?

아래와 같은 2차원 리스트나 튜플이 담고 있는 데이터를 루프를 돌면서 접근해야한다고 가정해봅시다.

```python
>>> matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
```

이 때 일반적으로 다음과 같이 중첩 `for` 문 내에서 행과 열의 인덱스로 데이터를 읽도록 작성을 많이 하실 거에요.

```python
>>> for r in range(len(matrix)):
...     for c in range(len(matrix[r])):
...             print(r, c, matrix[r][c])
...
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I
```

동일한 작업을 하는 코드를 `enumerate()` 함수를 이용해서 재작성하면 어떨까요?

```python
>>> for r, row in enumerate(matrix):
...     for c, letter in enumerate(row):
...             print(r, c, letter)
...
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I
```

코드가 더 깔끔하고 읽기 편하죠?! 🤗

예제 코드에서는 단순히 데이터를 출력만 하기 때문에 큰 차이를 못 느낄 수도 있지만, 실제 프로젝트에서 좀 더 복잡한 작업을 하는 경우라면 차이가 더 크게 날 거에요. 무엇보다도 2차원 배열을 다룰 때 인덱스를 사용하면 오타를 내기 쉬운데, `enumerate()` 함수를 사용하면 이러한 실수를 할 확률이 현저하게 줄어듭니다.

## 전체 코드

본 포스팅에서 제가 작성한 전체 코드는 아래에서 직접 확인하고 실행해보실 수 있습니다.
[https://dales.link/6in](https://dales.link/6in)

---
## [출처 링크][https://www.daleseo.com/python-enumerate/]
