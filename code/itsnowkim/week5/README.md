# 내 집 마련하기 boj-30619
문제 조건을 이해한 후, 자리를 바꿀 수 있는 사람들은 정렬한 순서대로 들어가면 조건에 만족한다는 것을 알게 되었다.

deepcopy 를 하지 않으면 원래 주어진 array 가 변하게 되므로 해당 부분에 유의해서 문제를 풀어야 한다.

# donstructive boj-30618
처음에 순열의 점수가 최대가 된다는 조건을 제대로 이해하지 못해서 문제 이해에 오래 걸렸다.

하지만, 가운데 위치한 숫자가 최대한 많이 나오도록 큰 수가 되어야 한다는 것을 이해한 후, 쉽게 풀 수 있었다.

# 보물섬 boj-2589
brute force 로 가장 긴 최단 거리를 출력하고자 했다.
처음에는 다음과 같이 했고, 메모리 초과로 실패했다.

```python
from collections import deque

direction = [(-1,0), (0,1), (1,0), (0,-1)]

def solution(x, y):
    if graph[x][y] == 'W':
        return 0
    
    # 땅일 경우, 갈 수 있는 모든 땅에 대해 탐색, 가장 먼 거리를 리턴
    visited = [[0]*W for _ in range(R)]
    longest = 0

    # 탐색 시작
    q = deque([(x, y, 0)])
    while q:
        curr_x, curr_y, dist = q.popleft()
        visited[curr_x][curr_y] = 1
        longest = max(longest, dist)

        for dir_x, dir_y in direction:
            next_x = curr_x + dir_x
            next_y = curr_y + dir_y

            # 갈 수 있으면 q 에 담기
            if 0<= next_x and next_x<R and 0<=next_y and next_y < W and graph[next_x][next_y] == 'L' and visited[next_x][next_y] != 1:
                q.append((next_x, next_y, dist+1))

    return longest

R, W = map(int, input().split())
graph = [input() for _ in range(R)]

# 최단 거리로 이동할 수 있는 거리 중, 가장 긴 거리?
answer = 0

for i in range(R):
    for j in range(W):
        temp = solution(i,j)
        answer = max(answer, temp)

print(answer)
```

그래서 distance 를 같이 q 에 넣지 않고, 넣기 전에 최댓값만 유지하도록 코드를 수정하였다. (업데이트만 함)

```python
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
```

성공!