# boj_2573 : 빙산
### code
```python
from collections import deque
from sys import stdin

n, m = map(int,stdin.readline().split())

board = []
year = 0

for i in range(n):
  board.append(list(map(int,stdin.readline().split())))

#N E S W  
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(gragh,x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    a, b = queue.popleft()
    visited[a][b] = True
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (0 <= nx < n and 0 <= ny < m and gragh[nx][ny] != 0 and visited[nx][ny] == False):
        visited[nx][ny] = True
        queue.append((nx,ny))

  return 1

while(True):
  ocean = [[0] * m for _ in range(n)]
  visited = [[0] * m for _ in range(n)]
  flag = 0
  iceberg = 0
  for x in range(n):
    for y in range(m):

      if board[x][y] != 0:
        flag = 1
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]

          if (0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0):
            ocean[x][y] += 1
  
  if (flag == 0):
    break

  for x in range(n):
    for y in range(m):
      board[x][y] -= ocean[x][y]

      if board[x][y] < 0:
        board[x][y] = 0

  year += 1

  #빙하 개수 세기
  for x in range(n):
    for y in range(m):
      if board[x][y] != 0 and visited[x][y] == False:
        iceberg += BFS(board,x,y)
  
  if iceberg > 1:
    break
  
if flag:
  print(year)
else:
  print(0)
  ```
## 결과
### 성공
## 접근
n과 m이 300 이하이기에 리스트를 순회하는 3중 반복문을 사용하여도 시간복잡도는 여유있을 것으로 판단하였다.

1. 입력받은 board의 빙하 주변 바다(0)의 개수를 ocean 리스트에 저장한다.

   -> 빙하를 바다의 개수대로 바로 녹일 경우 인접한 다른 빙하의 녹는 개수가 달라질 수 있기 때문에 한꺼번에 녹이기 위해 따로 저장
2. 빙하 주변 모든 바다의 개수를 다 구한 후 빙하를 녹인다.
3. 빙하가 녹은 이후 1년이 지났음을 표시하고 남은 빙하의 개수를 BFS를 이용해 구한다.
4. 빙하의 개수가 최초로 1개보다 많아질 경우 시간(년)을 출력한다.
5. 이때, 빙하가 모두 녹을 때까지 2개 이상으로 분리되지 않을 경우는 'flag'를 활용하여 처리해준다. 
## 문제 회고
문제를 풀기위한 아이디어는 비교적 빠르게 생각하였지만 구현 과정에서 잘못된 변수를 설정하고, while문안에 리스트를 넣지않아 초기화과정이 생략되는 등 실수가 많았다.

좀 더 문제를 꼼꼼하게 구현하도록 노력해야겠다.

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고

# prog_43163 : 단어변환
### code
```python
from collections import deque

def solution(begin, target, words):

    answer = 0
    words.append(begin)
    
    visited = [0 for _ in range(len(words))]
    gragh = [[] for _ in range(len(words))]

    if target not in words:
        return 0

    for i in range(len(words)):
        word = words[i]
        for j in range(len(words)):
            diff = 0
            for k in range(len(word)):
                if word[k] != words[j][k]:
                    diff += 1
            if diff == 1:
                gragh[i].append(j)
    
   
    # begin
    queue = deque([len(words) -1])
    visited[len(words)-1] = 1

    while queue:
        num = queue.popleft()
        if words[num] == target:
            answer = visited[num]-1
            break

        for i in gragh[num]:
            if visited[i] == 0:
                visited[i] = visited[num] + 1
                queue.append(i)
                
    return answer
  ```
## 결과
### 실패 후 풀이 참조
## 접근
1. 한개의 알파벳만 다른 단어들 사이 연결 리스트를 만든다.
2. begin부터 시작하여 target 단어까지 연결리스트 사이 최단 거리를 구한다.
3. words안에 target 단어가 없거나, target까지 리스트가 연결되지 않을 경우 0 을 return
## 문제 회고
문제를 처음 봤을 때 DFS/BFS 문제로 느껴지지 않고 낯설게 느껴졌다.
오랜 시간 고민해서 위의 접근을 생각하였지만, 구현에 실패하고 풀이를 참조하였다.

## 참고문헌
https://velog.io/@ledcost/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-43163-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98-level-3-BFSDFS

