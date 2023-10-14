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
        r, c = queue.popleft()
        for dy, dx in directions:
            dr = r + dy
            dc = c + dx

            if 0 <= dr < n and 0 <= dc < m:
                if iceberg[dr][dc] == 0:
                    visited[r][c] += 1

                if not visited[dr][dc] and iceberg[dr][dc] != 0:
                    queue.append((dr, dc))
                    visited[dr][dc] = True

time = 0
while True:
    count = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and iceberg[i][j] != 0:
                bfs(i, j)
                count += 1

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                iceberg[i][j] -= visited[i][j] - 1
                if iceberg[i][j] < 0:
                    iceberg[i][j] = 0

    time += 1
    if count == 0:
        break
    if count >= 2:
        flag = True
        break

if flag:
    print(time - 1)
else:
    print(0)

