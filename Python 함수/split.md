Python에서 `split()`을 사용하여 특정 문자를 기준으로 문자열을 분리할 수 있습니다.

Syntax는 다음과 같습니다.

```python
string.split(separator, maxsplit)
```

-   separator: 문자열을 나눌 때 사용할 문자입니다. 기본 값은 whitespace입니다.
-   maxsplit: 문자열을 나눌 횟수를 지정합니다. 기본 값은 -1이며, 제한 없이 모두 나눈다는 의미입니다.

예제와 함께 자세히 알아보겠습니다.

-   [1\. split() 예제](https://codechacha.com/ko/python-string-split/#1-split-%EC%98%88%EC%A0%9C)
-   [2\. split(separator, maxsplit) 예제](https://codechacha.com/ko/python-string-split/#2-splitseparator-maxsplit-%EC%98%88%EC%A0%9C)

## 1\. split() 예제

다음과 같은 문자열이 주어졌을 때, `split()`은 whitespace를 기준으로 문자열을 나눕니다.

```python
text = 'Hello world, python'
strings = text.split()
print(strings)
```

Output:

```python
['Hello', 'world,', 'python']
```

`split(',')`은 `,`를 기준으로 문자열을 나눕니다.

```python
text = 'Hello world, python'
strings = text.split(',')
print(strings)
```

Output:

```python
['Hello world', ' python']
```

다음과 같이 `:`로 나눌 수도 있습니다.

```python
text = 'Hello:world:python'
strings = text.split(':')
print(strings)
```

Output:

```python
['Hello', 'world', 'python']
```

## 2\. split(separator, maxsplit) 예제

maxsplit을 설정하면 최대 나눌 횟수를 지정할 수 있습니다.

다음과 같이, split(',', 0)는 `,`로 문자열을 나누지만 최대 0번까지만 나누라는 의미입니다.

```python
text = 'Hello, world, python'
strings = text.split(',', 0)
print(strings)
```

결과를 보면, 문자열을 나누지 않았고 문자열 전체가 리스트에 추가되었습니다.

`split(',', 1)`는 최대 1회까지만 문자열을 나눕니다.

```python
text = 'Hello, world, python'
strings = text.split(',', 1)
print(strings)
```

Output:

```python
['Hello', ' world, python']
```

`split(',', 2)`는 최대 2회까지 문자열을 나눕니다.

```python
text = 'Hello, world, python'
strings = text.split(',', 2)
print(strings)
```

Output:

```python
['Hello', ' world', ' python']
```

`split(',', -1)`는 횟수 제한 없이 나눌 수 있는 만큼 문자열을 나눕니다.

```python
text = 'Hello, world, python'
strings = text.split(',', -1)
print(strings)
```

Output:

```python
['Hello', ' world', ' python']
```

---
## [출처 링크](https://codechacha.com/ko/python-string-split)

