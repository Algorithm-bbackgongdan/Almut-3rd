import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

treasure_map = []

# N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#보물지도 그래프
for i in range(n):
  arr = []
  words = (sys.stdin.readline().rstrip())

  for word in words:
    arr.append(word)
  
  treasure_map.append(arr)

def BFS(treasure_map, x, y):
  visited = [[0 for _ in range(m)] for _ in range(n)]
  count = 0
  queue = deque()
  visited[x][y] = 1
  queue.append((x,y))

  while queue:
    a, b = queue.popleft()
  
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (nx < 0 or nx >= n or ny < 0 or ny >= m):
        continue
      elif(treasure_map[nx][ny] == 'L' and visited[nx][ny] == 0):
        visited[nx][ny] = visited[a][b] + 1
        count = max(count, visited[nx][ny])
        queue.append((nx,ny))

  return count-1

result = 0
for i in range(n):
  for j in range(m):
    if treasure_map[i][j] == 'L':
      result = max(result, BFS(treasure_map,i,j))

print(result)

