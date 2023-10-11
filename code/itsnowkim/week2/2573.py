import sys
from collections import deque

def dfs(visited, x,y, R, C):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    visited[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx and nx<R and 0<=ny and ny<C and visited[nx][ny] == 0 and graph[nx][ny]>0:
            visited[nx][ny] = 1
            dfs(visited, nx, ny, R, C)
    
        return visited

def bfs(visited, x,y, R,C):
    q = deque([(x,y)])
    visited[x][y] = 1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx and nx<R and 0<=ny and ny<C and visited[nx][ny] == 0 and graph[nx][ny]>0:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return visited

# 몇 개의 조각인지 체크
def devided(graph, R, C):
    answer = 0
    visited = [[0]*C for _ in range(R)]
    flag = 0

    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0 and visited[i][j] == 0:
                visited = bfs(visited, i, j, R, C)
                answer += 1
                flag = 1

    # 두 조각 이상으로 분리 안 되는 경우에는 0을 출력
    if flag == 0:
        print(0)
        sys.exit()

    # print('answser : ', answer)
    return answer

# for loop 돌면서 붙어있는거 체크
def year_pass(graph, R, C):
    temp = [[0]*C for _ in range(R)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(R):
        for j in range(C):
            count = 0
            for x, y in zip(dx, dy):
                next_x = i + x
                next_y = j + y
                if 0 <= next_x and next_x < R and 0 <= next_y and next_y < C and graph[next_x][next_y] == 0:
                    count += 1
            
            temp[i][j] = count
    
    for i in range(R):
        for j in range(C):
            graph[i][j] = max(graph[i][j] - temp[i][j], 0)

    return graph

# main
if __name__ == "__main__":
    R,C = map(int, input().split(' '))
    graph = [list(map(int, input().split(' '))) for _ in range(R)]
    temp = [[0]*C for _ in range(R)]
    
    year = 0

    while devided(graph, R, C) < 2:
        graph = year_pass(graph, R, C)
        year += 1

    print(year)