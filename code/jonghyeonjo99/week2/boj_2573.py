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