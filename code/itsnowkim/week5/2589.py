from collections import deque

direction = [(-1,0), (0,1), (1,0), (0,-1)]

def solution(x, y):
    # 땅일 경우, 갈 수 있는 모든 땅에 대해 탐색, 가장 먼 거리를 리턴
    visited = [[0]*W for _ in range(R)]
    longest = 0

    # 탐색 시작
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        curr_x, curr_y = q.popleft()
        
        for dir_x, dir_y in direction:
            next_x = curr_x + dir_x
            next_y = curr_y + dir_y

            # 갈 수 있으면 q 에 담기
            if 0<= next_x and next_x<R and 0<=next_y and next_y < W and graph[next_x][next_y] == 'L' and visited[next_x][next_y] == 0:
                q.append((next_x, next_y))
                visited[next_x][next_y] = visited[curr_x][curr_y] + 1
                longest = max(longest, visited[next_x][next_y])

    return longest-1

R, W = map(int, input().split())
graph = [input() for _ in range(R)]

# 최단 거리로 이동할 수 있는 거리 중, 가장 긴 거리?
answer = 0

for i in range(R):
    for j in range(W):
        if graph[i][j] == 'L':
            temp = solution(i,j)
            answer = max(answer, temp)

print(answer)