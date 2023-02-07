#### Date : 2023-02-07

### 문제 : String Permutation (14534번)
---
## 문제

(String permutation) Write a recursive method to print all the permutations of a string. The user need to enter the string which consists of a set of characters.

## 입력

First line of the input contains _T_ (1 ≤ _T_ ≤ 200), the number of test cases. For each test case, there will a string of characters, _L_ (1 ≤ _L_ ≤ 5).

## 출력

For each test case, output a line in the format “Case # x:” where x is the case number (starting with 1), follow by the set of string permutation.

## 예제 입력 1 복사

```
3
abc
zxyw
p7*

```

## 예제 출력 1 복사

```
Case # 1:
abc
acb
bac
bca
cab
cba
Case # 2:
zxyw
zxwy
zyxw
zywx
zwxy
zwyx
xzyw
xzwy
xyzw
xywz
xwzy
xwyz
yzxw
yzwx
yxzw
yxwz
ywzx
ywxz
wzxy
wzyx
wxzy
wxyz
wyzx
wyxz
Case # 3:
p7*
p*7
7p*
7*p
*p7
*7p
```

---
### 코드 작성
```python
def dfs(n):
    if len(num) == len(L):
        print("".join(num))
        return

    for i in range(len(L)):
        if check[i] == False:
            check[i] = True
            num.append(L[i])
            dfs(i)
            check[i] = False
            num.pop()

T = int(input())
for i in range(1, T+1):
    L = input()
    num = []
    check = [False]*len(L)

    print(f'Case # {i}:')
    dfs(0)
```

---
### 코드 설명
<br/>

```python
T = int(input())
for i in range(1, T+1):                  ───(1)
    L = input()                          ──┘
    num = []                             ───(2)
    check = [False]*len(L)               ──┘

    print(f'Case # {i}:')                ───(3) 
    dfs(0)                               ──┘
```
- (1) 테스트 케이스 수`T` 만큼 테스트 케이스 `L`를 입력합니다
- (2) 조건에 맞는 테스트 케이스`L`를 담아줄 리스트`num`을 생성합니다
- (2) 또한 방문처리 역할인 bool형이 담긴 리스트`check`를 생성합니다

---
### 참고 자료