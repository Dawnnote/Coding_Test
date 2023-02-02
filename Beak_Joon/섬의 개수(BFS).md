#### Date : 2023-02-02

### 문제 : 섬의 개수 (4963번)
---
## 문제 설명

정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

![](https://www.acmicpc.net/upload/images/island.png)

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

## 출력

각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

## 예제 입력 1

```
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
```

## 예제 출력 1

```
0
1
1
3
1
9
```

---
### 코드 작성

```python
from collections import deque
import sys

def bfs(a, b):
    mx = [-1, 1, 0, 0, -1, -1, 1, 1]
    my = [0, 0 ,-1, 1, -1, 1, -1, 1]
    
    q = deque([(a, b)])
    MAP[a][b] = 2
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + mx[i]
            ny = y + my[i]
            
            if 0 <= nx < h and 0 <= ny < w and MAP[nx][ny] == 1:
                MAP[nx][ny] = 2
                q.append((nx, ny))

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
```

---
### 코드 설명
<br/>

```python
while True:
    w, h = map(int, sys.stdin.readline().split())  
    if not w and not h:                            ---(1)
        break
```
- (1) 너비`w` 와 높이`h`가 `0`이라면 while문을 멈춘다

<br/>
<br/>

```python
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]  ───(1)
    cnt = 0                                                                 ──┘
    
    for i in range(h):               ───(2)
        for j in range(w):               │
            if MAP[i][j] == 1:           │
                bfs(i, j)                │
                cnt += 1             ────┘
    print(cnt)                       ---(3)
```
- (1) 높이`h` 만큼 MAP 행을 만들어 주고, 섬의 개수를 카운트 해주기위해 `cnt`변수를 선언해줍니다

- (2) 높이`h`와 너비`w`만큼 반복문을 돌려서 `MAP` 전체 값을 확인 해줍니다. 이때, 
  `MAP`의 해당 위치가 섬(`1`)인 경우만 `bfs()` 라는 함수에 `(i, j)` 위치를 넣어줍니다. 
  `1`은 섬이 있다는 말이기 때문에 `cnt`변수에 1를 증가 시켜줍니다

- 반복문이 모두 끝나면 (3) 섬의 개수를 출력해줍니다

<br/>
<br/>

##### bfs 함수 부분 (1)
```python
def bfs(a, b):
    mx = [-1, 1, 0, 0, -1, -1, 1, 1]           ───(1)
    my = [0, 0 ,-1, 1, -1, 1, -1, 1]           ───┘
    
    q = deque([(a, b)])                        ───(2)
    MAP[a][b] = 2                              ───┘

```
- (1) 상, 하, 좌, 우, 대각선이 담긴 `mx`, `my` 리스트 변수를 만들어 줍니다
  ex) (`mx[0]`, `my[0]`) → (-1, 0) → 위(상)

- (2) 위치 인덱스를 받은 `a`, `b` 를 2차원 형태로 `deque` 에 담아줍니다
   `MAP[a][b]`위치의 값이 `1`로 되어있는 것을  `2`로 바꿔 방문처리 해줍니다
   (`0`으로 바꿔도 됩니다)

<br/>
<br/>

##### bfs 함수 부분(2)
```python
    while q:                              ---(1)
        x, y = q.popleft()                ---(2)
        
        for i in range(8):                ───(3)
            nx = x + mx[i]                   │
            ny = y + my[i]                ───┘
            
            if 0 <= nx < h and 0 <= ny < w and MAP[nx][ny] == 1:    ───(4)
                MAP[nx][ny] = 2                                         │
                q.append((nx, ny))                                  ────┘
```
- (1) 큐`q` 가 비어질때까지 다음 명령들을 반복합니다

- (2) 큐`q` 안에 위치인덱스 들이 담긴 `a`, `b`를 앞에서부터 `pop`을 해서
   `x`에는 `a`값, `y`에는 `b`값을 담아줍니다

- (3) 해당 위치에서 상, 하, 좌, 우, 대각선 들의 모든 값을 알기 위해 8번 반복해줍니다
  `nx`값에는 현재 `x`위치와 `mx`의 `i`번째 값
  `ny`값에는 현재 `y`위치와 `my`의 `i`번째 값

- (4) 위치정보는 너비`w`와 높이`h`을 넘어가서는 안되고 0보다 작아도 안됩니다 그래서
  `nx` 는 `0`보다 크거나 같고, `nx`의 위치는 높이`h`와 관련이 있기 때문에 높이`h`보다 작아야 됩니다
  `ny`도 마찬가지로 `0`보다 크거나 같고, 너비`w`와 관련이 있으므로 너비`w`보다 작아야 됩니다

- 위 (4) 조건과 맞으면, `MAP`의 (`nx`, `ny`)위치의 값을 2로 바꾸어 방문처리 해줍니다
- 방문처리한 `nx`, `ny` 의 위치값을 q로 다시 append 시켜줍니다

- `MAP`의 섬이 모두 확인되면 `cnt`변수에 섬의 개수만큼 증가시킨 후 출력합니다

---
### 참고 자료
