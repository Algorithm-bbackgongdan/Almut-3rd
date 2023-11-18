# Week 5

# 30619 : 내 집 마련하기
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys

N = int(sys.stdin.readline().rstrip())
A = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
for _ in range(M):
  L, R = map(int, sys.stdin.readline().rstrip().split())
  tmp = L
  for i in range(1,N+1):
    if L <= A[i] <= R:
      print(tmp, end=" ")
      tmp += 1
    else:
      print(A[i], end=" ")
  print()
```

### ❗️ 결과

성공

### 💡 접근

L ~ R에 해당하는 숫자를 오름차순으로 배치하기만 하면 되는 문제였다. 따라서 L ~ R 범위 이외의 숫자는 그대로 출력하고, L ~ R 범위 이내의 숫자는 L부터 R까지 오름차순으로 출력하면 된다.

## 🥳 문제 회고

답을 구하는 과정은 금방 생각했지만, 구현은 어떻게 할지 조금 시간이 걸렸던 문제다.

# 30618 : donstructive
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys

N = int(sys.stdin.readline().rstrip())
P = [0]*(N+1)
for i in range(1,N+1):
  if i % 2 == 1:
    P[i//2 + 1] = i
  else:
    P[N-i//2 + 1] = i

for e in P[1:]:
  print(e, end=" ")
```

### ❗️ 결과

성공

### 💡 접근

최댓값이 나오는 경우를 생각해보면, 수열의 중앙에 가까이 위치할수록 큰 수를 배치해야 한다. 따라서, 1 ~ N까지 순회하며 양끝부터 중앙 방향으로 차례대로 수를 할당하면 된다.

## 🥳 문제 회고

최대가 되는 경우를 금방 생각할 수 있었다. 미리 리스트를 만들고 값을 할당하는 방식으로 구현했는데, deque를 써도 될 것 같다.

# 2589 : 보물섬
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys
from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]
global answer

answer = 0
N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
  board.append(sys.stdin.readline())

#bfs
def bfs(y,x):
  global answer
  visited = [[0]*M for _ in range(N)]
  q = deque([]);
  q.append((y,x))
  visited[y][x] = 1
  while q:
    cy, cx = q.popleft()
    answer = max(answer, visited[cy][cx])
    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if (ny < 0 or ny >= N or nx < 0 or nx >= M): continue
      if (board[ny][nx] == 'W' or visited[ny][nx] != 0): continue
      visited[ny][nx] = visited[cy][cx] + 1
      q.append((ny,nx))

for i in range(N):
  for j in range(M):
    if board[i][j] == 'W': continue
    bfs(i,j)
print(answer - 1)
```

### ❗️ 결과

성공

### 💡 접근

모든 L을 시작점으로 했을 때 BFS를 통해 가장 멀리 도달할 수 있는 거리를 구하고, 그 중 최댓값을 구한다.

DFS를 사용하면 최단거리라도 돌아가는 경우가 생길 수 있기 때문에 BFS를 이용해 구해야 한다.

## 🥳 문제 회고

접근 자체는 쉬웠지만, 메모리 초과가 떠서 메모리를 줄이느라 힘들었다.