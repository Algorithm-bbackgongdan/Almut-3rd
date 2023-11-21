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