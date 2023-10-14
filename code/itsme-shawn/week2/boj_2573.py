import sys
from collections import deque

read = sys.stdin.readline


n, m = map(int,read().split())
board = [list(map(int,read().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0 # 빙산 덩어리 개수
day = 0
flag = False

deq = deque()


def bfs(x,y):
    deq.append((x,y))
    while deq:
        print(1)
        x,y = deq.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] and visited[nx][ny] != 0: # 미방문한 빙산에 대해
                    visited[nx][ny] = 1
                    deq.append((nx,ny))
                elif board[nx][ny] == 0:
                    cnt[x][y] += 1 # bfs를 시작한 빙산이 깎일 횟수 계산
                

while True:
    visited = [[0]*m for _ in range(n)]
    cnt = [[0]*m for _ in range(n)] # 해당 빙산이 깎일 횟수
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j]: # 미방문한 빙산에 대해 bfs
                # print(2)
                bfs(i,j)
                res += 1 # 빙산 덩어리 개수 증가
                
        
    for i in range(n):
        for j in range(m):
            if cnt[i][j]:
                board[i][j] -= cnt[i][j]
                if board[i][j] < 0:
                    board[i][j] = 0
              
    day += 1      
    
    if res == 0:
        break
    if res >= 2:
        flag = True
        break

if flag:
    print(day-1)
else:
    print(0)
                
                
                
    

