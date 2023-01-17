### 파이썬의 사전(dictionary) 사용법
<iframe src="https://www.youtube.com/embed/yUxVfv28Tbw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen=""></iframe>

사전(dictionary)은 파이썬에서 리스트(list)와 더불어 가장 널리 사용되는 내장 자료형입니다. 하지만 너무 기본적인 기능이다 보니 호히려 이 중요한 자료형의 사용법을 제대로 익히지 않고 넘어가기 쉬운 것 같아요.

이번 포스팅에서는 파이썬에서 사전을 어떻게 사용하는지에 대해서 차근차근 알아보도록 하겠습니다.

## 사전의 특징

해시 테이블(hash table)이라는 자료 구조를 기반으로 하는 사전은 키(key)와 값(value)으로 이루어진 여러 쌍의 데이터를 담기 위해서 사용하는데요. 파이썬의 리스트처럼 가변(mutable) 자료형이기 때문에 사전을 생성 후에 자유롭게 새로운 키에 값을 추가하거나 기존 키의 값을 변경 또는 삭제할 수 있습니다.

동적 언어인 파이썬에서는 키로 해시가 가능한(hashable) 모든 데이터를 사용할 수 있고, 값에 대해서는 아무런 제한없이 어떤 자료형의 데이터도 저장할 수 있는데요. 자바(Java)와 같이 선언할 때 명시한 자료형의 키와 값만 사용하도록 제한하는 정적 타이핑 언어와 비교했을 때 상당히 대조되는 부분입니다.

같은 동적 언어 계열인 자바스크립트(JavaScript)에 익숙하시다면 자연스럽게 객체(object)를 떠올리시게 되실텐데요. 자바스크립트의 객체는 값으로 아무런 데이터나 저장할 수 있다는 측면에서는 파이썬의 사전과 유사하지만, 자바스크립트의 객체는 키로 문자열이나 숫자, 심볼(symbol)만 사용할 수 있다는 점에서 약간의 차이점이 있겠습니다.

> 사전과 비슷한 특징을 가지되 담고 있는 데이터가 불변(immutable)해야 한다면 named tuple을 사용해야 합니다. 이 부분은 [관련 포스팅](https://www.daleseo.com/python-immutable-datatypes/)를 참고 바랍니다.

## 사전 생성

사전을 생성하는 데는 여러가지 방법이 있지만, 가장 많이 사용되는 방법은 중괄호(`{}`)를 사용하는 것인데요. 중괄호 안에 `<키>: <값>` 형태의 데이터 쌍을 쉼표(`,`)로 구분해서 나열해주면 됩니다.

예를 들어, 사용자의 정보를 담아두기 위한 사전은 다음과 같이 생성할 수 있습니다.

```
>>> { "name": "사용자", "email": "user@test.com", "age": 25 }
{'name': '사용자', 'email': 'user@test.com', 'age': 25}
```

사실 빈 사전을 생성할 때도 자주 있는데요. 가변 자료형이라 나중에 언제든지 데이터를 추가할 수 있기 때문입니다. 빈 사전을 생성할 때는 빈 중괄호를 사용하거나, `dict()` 내장 함수를 호출하면 됩니다.

자주 쓰이는 방법은 아니지만, `dict()` 내장 함수의 키워드 인자를 사용하거나, 키와 값을 담은 튜플(tuple)의 리스트를 인자로 넘길 수도 있습니다.

```
>>> dict(name="사용자", email="user@test.com", age=25)
{'name': '사용자', 'email': 'user@test.com', 'age': 25}
>>> dict([("name", "사용자"), ("email", "user@test.com"), ("age", 25)])
{'name': '사용자', 'email': 'user@test.com', 'age': 25}
```

## 데이터 추가

사전에 데이터를 추가할 때는 대괄호(`사전[<키>] = <값>`)를 사용하여 원하는 값을 할당해주면 됩니다.

```
>>> user = {}
>>> user["name"] = "사용자"
>>> user["email"] = "user@test.com"
>>> user["age"] = 25
>>> user
{'name': '사용자', 'email': 'user@test.com', 'age': 25}
```

## 데이터 접근

사전이 담고 있는 데이터에 접근할 때도 대괄호(`사전[<키>]`)를 사용합니다.

```
>>> user["name"]
'사용자'
>>> user["email"]
'user@test.com'
>>> user["age"]
25
```

한 가지 주의할 점은 사전에 존재하지 않는 키를 사용하면 `KeyError` 오류가 발생한다는 것입니다.

```
>>> user["mail"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'mail'
```

이러한 오류를 방지하고 싶다면, 사전의 `get(<키>[, <기본값>])` 메서드를 사용하면 됩니다. 기본값을 지정해주지 않으면, 키가 존재하지 않을 때, `None`을 반환합니다.

```
>>> user.get("mail", "서울")
'서울'
>>> user.get("mail") == None
True
```

사전에 어떤 키가 존재하는지 안 하는지 확실하지 않을 때는 대괄호 대신에 `get()` 메서드를 사용하는 것이 좀 더 안전한 데이터 접근이 될 것입니다.

## 데이터 갱신

가변 자료형인 사전은 자유롭게 담고 있는 데이터를 갱신할 수 있습니다. 기존 키에 새로운 값을 할당하기만 하면 기존 값이 새로운 값으로 대체됩니다.

```
>>> user["age"] = 31
>>> user
{'name': '사용자', 'email': 'user@test.com', 'age': 31}
```

## 데이터 삭제

`del` 키워드를 사용해서 특정 키와 값의 쌍을 사전에서 제거할 수 있습니다.

```
>>> del user["email"]
>>> user
{'name': '사용자', 'age': 31}
```

## 사전 순회

`in` 연산자를 통해서 사전에 있는 모든 데이터를 `for` 루프문으로 순회할 수 있는데요. 기본적으로는 키만 얻어지기 때문에, 값은 대괄호를 이용해서 접근해야 합니다.

```
>>> user = {"name": "사용자", "email": "user@test.com", "age": 25}
>>> for key in user:
...     print(f"{key}: {user[key]}")
...
name: 사용자
email: user@test.com
age: 25
```

하지만 사전의 `items()` 메서드를 활용하면 키와 값을 튜플의 형태로 한 번에 얻을 수 있어서 좀 더 깔끔하게 루프문을 작성할 수 있습니다.

```
>>> user = {"name": "사용자", "email": "user@test.com", "age": 25}
>>> for key, value in user.items():
...     print(f"{key}: {value}")
...
name: 사용자
email: user@test.com
age: 25
```

## 키 존재 여부 확인

`in` 연산자를 사용하면 특정 키가 사전에 존재하는지도 쉽게 확인 할 수 있습니다.

```
>>> user = {"name": "사용자", "email": "user@test.com", "age": 25}
>>> "email" in user
True
>>> "mail" in user
False
```

따라서 `if` 조건문과도 자연스럽게 함께 사용할 수 있습니다.

```
>>> if "email" in user:
...     print("email 키는 존재합니다.")
... else:
...     print("email 키를 사전에서 찾을 수 없습니다.")
...
email 키는 존재합니다.
```

## 사전 병합

여러 개의 사전을 합쳐야할 때는 `**` 연산자를 사용하여, 중괄호 안에 합칠 사전들을 쉼표(`,`)로 구분하여 나열하면 됩니다. (자바스크립트 개발자라시면 `...` 연산자가 떠오르실 거에요 😉)

```
>>> dic1 = {"A": 1, "B": 2}
>>> dic2 = {"B": 3, "C": 4}
>>> { **dic1, **dic2 }
{'A': 1, 'B': 3, 'C': 4}
```

Python 3.9 버전부터는 대신에 `|` 연산자를 사용해서 좀 더 깔끔하게 여러 개의 사전을 병합할 수 있습니다.

```
>>> dic1 | dic2
{'A': 1, 'B': 3, 'C': 4}
```

## 사전 반영

하나의 사전에 다른 사전의 모든 데이터를 반영하고 싶을 때는 사전의 `update()` 메서드를 사용할 수 있습니다.

```
>>> dic1 = {"A": 1, "B": 2}
>>> dic2 = {"B": 3, "C": 4}
>>> dic1.update(dic2)
>>> dic1
{'A': 1, 'B': 3, 'C': 4}
```

바로 위에서 다룬 단순 병합과 달리 기존 사전에 있는 데이터에 직접적인 변경이 가해지는 점을 주의 바라겠습니다.

마찬가지로 Python 3.9 버전에서 사전에 추가된 `|` 연산자를 활용해서 같은 효과를 낼 수도 있습니다.

```
>>> dic1 = {"A": 1, "B": 2}
>>> dic2 = {"B": 3, "C": 4}
>>> dic1 |= dic2
>>> dic1
{'A': 1, 'B': 3, 'C': 4}
```

## 전체 코드

본 포스팅에서 제가 작성한 전체 코드는 아래에서 직접 확인하고 실행해보실 수 있습니다.

[https://deepnote.com/workspace/dale-seo-dc7078e7-0cb4-468a-9bd6-576063fa0466/project/Blog-61ddfe0e-c57f-41e1-aaa3-801467b1721e/%2Fpython-ditonary.ipynb](https://deepnote.com/workspace/dale-seo-dc7078e7-0cb4-468a-9bd6-576063fa0466/project/Blog-61ddfe0e-c57f-41e1-aaa3-801467b1721e/%2Fpython-ditonary.ipynb)

---
>[출처 링크][https://www.daleseo.com/python-ditonary/]


