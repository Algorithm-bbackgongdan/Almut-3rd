# Week 7

# 2629 : 양팔 저울
- 출처 : 백준

## 🥺 Unsolved Code

### 💻 Code

```python
import sys

MAX_MARBLE_WEIGHT = 40001
MAX_WEIGHT = 500

n = int(sys.stdin.readline().rstrip()) # 추 개수
weights = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip()) # 구슬 개수
marbles = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[False]*(MAX_MARBLE_WEIGHT+MAX_WEIGHT) for _ in range(n)] #(추 최대 개수 x 구슬 최대 무게)

# init dp
for i in range(n):
  dp[i][0] = True
for i in range(n):
  dp[i][weights[i]] = True

for i in range(n):
  for j in range(1, MAX_MARBLE_WEIGHT):
      # 추 안 올림
      if i > 0: dp[i][j] |= dp[i-1][j]
      # 구슬과 같은 쪽에 추 올림
      dp[i][j] |= dp[i-1][weights[i] + j]
      # 구슬과 반대 쪽에 추 올림
      dp[i][j] |= dp[i-1][abs(weights[i] - j)]

for marble in marbles:
  if dp[-1][marble]:
    print("Y", end=" ")
  else:
    print("N", end=" ")
print()
```

### ❗️ 결과

실패 - 반례 발견

```
# 반례
3
20 35 50
1
5

정답 : Y
```

### 💡 접근

Knapsack 문제에서 착안하여 DP로 접근하고자 했다. 2차원 리스트 dp는 “추 최대 개수 x 구슬 최대 무게” 사이즈를 갖고있다. 

- dp[i][j]:  0 ~ i번째 추를 갖고 있을 때, 무게가 j인 구슬을 측정할 수 있는지 여부를 저장한다.

무게가 0인 구슬은 반드시 측정 가능하고, 갖고있는 추와 동일한 무게는 즉시 측정 가능하므로 해당 경우들은 True로 초기화 한다.

이후 bottom-top 방식으로 순회하며 dp 리스트를 채운다. 다음과 같은 경우가 있을 수 있다.

- 추를 안 올리는 경우
- 추를 구슬쪽에 올리는 경우
- 추를 구슬 반대쪽에 올리는 경우

3가지에 대해 확인하며 dp[i][j]를 업데이트 한다.

### 🧐 접근에 대한 회고

계속 틀려서 질문 게시판을 보니 반례가 존재했다. 내 알고리즘으로는 해결할 수 없는 케이스였다. 구글링을 해보니 dp를 활용하는 접근법은 맞지만, 내가 놓친게 있던 것 같다.


# 2841 : 외계인의 기타 연주
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
import sys

N, P = map(int, sys.stdin.readline().rstrip().split())
melodys = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

answer = 0
stacks = [[] for _ in range(N+1)]
for n, p in melodys:
  if len(stacks[n]) == 0 or stacks[n][-1] < p:
    answer += 1
    stacks[n].append(p)
  elif p < stacks[n][-1]:
    while stacks[n] and p < stacks[n][-1]:
      stacks[n].pop()
      answer += 1
    if len(stacks[n]) == 0 or stacks[n][-1] < p:
      stacks[n].append(p)
      answer += 1
print(answer)
```

### ❗️ 결과

성공

### 💡 접근

한 번 누른 프랫은 최대한 오랫동안 안떼야만 최소한으로 손가락을 움직일 수 있다. 

예를 들어 1,2,5 프랫을 차례대로 누른 상태에서 다음으로 4프랫을 누르는 상황이 있다. 이 때 5프랫만 떼고, 4프랫을 새로 누르는 것이 최소한의 움직임이다.

위 논리를 구현하기 위해 기타 줄마다 누른 프랫을 오름차순으로 저장하는 stack을 사용했다.

## 🥳 문제 회고

어떤 경우에  최소한의 움직임을 가져갈 수 있는지 금방 찾을 수 있는 문제였다. 다만 구현시에 예외처리(ex. stack 비어있음 등)를 위해 신경을 써야했다.


# 84021 : 퍼즐 조각 채우기
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]

'''
블록 탐색
- search blocks: 블록 조각들 반환
- bfs: 블록 조각 1개 탐색
- out_of_range: bfs 과정 중 좌표 유효성 검사
'''
def search_blocks(board, tile): #(보드, 탐색할 숫자)
    N = len(board)
    visited = [[False]*N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == tile and not visited[i][j]:
                blocks.append(bfs(i, j, board, tile, N, visited))
    return blocks

def bfs(y,x,board,tile, N, visited):
    q = deque([(y,x)])
    block = [(y,x)]
    visited[y][x] = True
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if out_of_range(ny,nx,N) or visited[ny][nx] or board[ny][nx] != tile: continue
            q.append((ny,nx))
            visited[ny][nx] = True
            block.append((ny,nx))
    return block

def out_of_range(y,x,N):
    return (y < 0 or y >= N or x < 0 or x >= N)

'''
블록 전처리 (직사각형으로 감싸기)
- preprocess_blocks: 전처리된 블록 조각들 반환
- preprocess: 블록 조각 1개 전처리
'''
def preprocess_blocks(blocks):
    preprocessed_blocks = []
    for block in blocks:
        preprocessed_blocks.append(preprocess(block))
    return preprocessed_blocks

def preprocess(block):
    min_y, min_x, max_y, max_x = 50, 50, 0, 0
    for y,x in block:
        min_y, min_x = min(min_y, y), min(min_x, x)
        max_y, max_x = max(max_y, y), max(max_x, x)
    N, M = (max_y - min_y + 1), (max_x - min_x + 1) # (높이, 너비)
    preprocessed = [[0]*M for _ in range(N)]
    for y,x in block:
        preprocessed[y-min_y][x-min_x] = 1
    return preprocessed

'''
최대 점수 계산
- compare_blocks: 두 블록 조각 모음을 비교해 최대 점수 반환
- same_matrix_size: 두 블록이 같은 크기의 Matrix로 표현되는지지 비교 (90도 회전시 같아도 same)
- same: 두 블록을 4번 90도 회전시켜 같은지 비교
- rotate: 블록 90도 회전
- compare: 두 블록이 정확히 같은지 비교
- size: 블록의 크기 (1의 개수)
'''
def compare_blocks(A, B):
    answer = 0
    used_A = [False]*len(A)
    used_B = [False]*len(B)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if used_A[i] or used_B[j]: continue # 이미 채워 넣은 조각은 건너 뜀
            if not same_matrix_size(a,b): 
                continue
            if same(a,b): 
                answer += size(a)
                used_A[i] = used_B[j] = True
    return answer

def same_matrix_size(A,B):
    h_A, w_A = len(A), len(A[0])
    h_B, w_B = len(B), len(B[0])
    return (h_A == h_B and w_A == w_B) or (h_A == w_B and w_A == h_B)

def same(A,B):
    h_A, w_A = len(A), len(A[0])
    for _ in range(4):
        B = rotate(B)
        h_B, w_B = len(B), len(B[0])
        if (h_A != h_B) or (w_A != w_B): continue
        if compare(A,B,h_A,w_A):
            return True
    return False

def rotate(block):
    rotated = [list(l) for l in zip(*block[::-1])]
    return rotated

def compare(A,B,H,W):
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]: return False
    return True

def size(block):
    answer = 0
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1: answer += 1
    return answer

'''
Main Solution 함수
'''
def solution(game_board, table):    
    # table에서 조각 모으기
    blocks = preprocess_blocks(search_blocks(table, 1))
    
    # game_board에서 빈 조각 모으기
    emptys = preprocess_blocks(search_blocks(game_board, 0))

    # 비교하기    
    return compare_blocks(blocks,emptys)
```

### ❗️ 결과

성공

### 💡 접근

1. bfs로 블록 조각, 인접한 빈 공간들의 좌표를 모은다
2. 모은 좌표들을 직사각형 형태로 전처리한다
    
    ```python
    '''
    ##
     #
     ##
    모양의 블록
    '''
    block = [(0,3),(0,4),(1,4),(2,4),(2,5)]
    preprocessed = [
    	[1,1,0],
    	[0,1,0],
    	[0,1,1]
    ]
    ```
    
3. 빈 공간 조각들과 블록 조각들을 90도로 4번 회전하며 비교한다
4. 일치하면 answer += 블록크기

## 🥳 문제 회고

호흡이 상당히 긴 문제였다. 구현 내용 하나하나를 함수로 잘 쪼개는게 중요한 문제였다.