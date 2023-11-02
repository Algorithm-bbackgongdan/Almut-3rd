from collections import deque

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
flag = False

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        r, c = queue.popleft() # row, col
        for dy, dx in directions:
            nr = r + dy # next row
            nc = c + dx # next col

            if 0 <= nr < n and 0 <= nc < m:
                if iceberg[nr][nc] == 0: # 주변이 빙산이 아니라면 (바다라면)
                    visited[r][c] += 1 # 깎을 빙산 수 증가
 
                if not visited[nr][nc] and iceberg[nr][nc] != 0: # 미방문한 빙산에 대해
                    queue.append((nr, nc))
                    visited[nr][nc] = True

time = 0
while True:
    count = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and iceberg[i][j] != 0:
                bfs(i, j)
                count += 1 # 빙산 개수 증가

    # bfs 다 돌린 후 빙산의 높이 감소 시키기
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                iceberg[i][j] -= visited[i][j] - 1
                if iceberg[i][j] < 0:
                    iceberg[i][j] = 0

    time += 1
    if count == 0: # 분리된 빙산이 없는 경우
        break
    if count >= 2:
        flag = True
        break

if flag:
    print(time - 1)
else:
    print(0)

