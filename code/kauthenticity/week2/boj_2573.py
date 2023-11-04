from sys import stdin
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def meltIceberg():
    global n, m, board
    meltings = [] # (row, col, cnt)

    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                continue

            cnt = 0 # 주변 바다의 개수

            for dirX, dirY in directions:
                newX, newY = x + dirX, y + dirY

                if newX < 0 or newX >= n or newY < 0 or newY >= m:
                    continue

                if board[newX][newY] == 0:
                    cnt += 1

            if cnt > 0:
                meltings.append((x, y, cnt))

    for row, col, cnt in meltings:
        board[row][col] = max(0, board[row][col] - cnt)

    return

def solution():
    global n, m, board

    answer = 0

    sea = 0
    for row in board:
        sea += row.count(0)

    # 바다가 없어서 녹지 못함
    if sea == 0:
        return 0

    while True:
        visited = set()
        icebergCnt = 0

        # 빙산의 개수 카운트
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 or (i, j) in visited:
                    continue

                queue = deque([])

                visited.add((i, j))
                queue.append((i, j))
                icebergCnt += 1

                while queue:
                    curX, curY = queue.popleft()

                    for dirX, dirY in directions:
                        newX, newY = curX + dirX, curY + dirY

                        if newX < 0 or newX >= n or newY< 0 or newY >=m or (newX, newY) in visited or board[newX][newY] == 0:
                            continue

                        queue.append((newX, newY))
                        visited.add((newX, newY))
        
        # 빙산이 분리됨
        if icebergCnt >= 2:
            break

        # 다 녹아서 없음
        elif icebergCnt == 0:
            answer = 0
            break

        meltIceberg()
        answer += 1

    return answer


n, m = map(int, stdin.readline().rstrip().split())
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

print(solution())
