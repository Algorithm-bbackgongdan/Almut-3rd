# 2주차

## 1. 백준\내 집 마련하기 (30619)

### 💡 Idea

주어진 쿼리에서 사람번호가 큰 사람이 집 번호가 큰 곳에 들어가도록 해주면 된다.

1. 각 사람들이 몇 번 집인지 저장해놓기 (dict를 사용)
2. 쿼리를 받아서 쿼리의 사람들이 몇 번 집인지 저장
3. 해당 집 번호를 sort
4. 작은 집 번호에 작은 번호 사람이 들어가도록 해주기

### 🧑🏻‍💻 Code

```python
N = int(input())
A = list(map(int, input().split()))
M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]

# 각 사람이 몇 번 집인지 dict로 저장
dic = {}
for i in range(N):
    dic[A[i]] = i + 1

for query in queries:
    houses = []
    A_copy = A[:]
    for j in range(query[0], query[1] + 1):
        houses.append(dic[j])
    houses.sort()

    people = list(range(query[0], query[1] + 1))

    for i in range(len(houses)):
        A_copy[houses[i] - 1] = people[i]

    print(*A_copy)


```

## 2. 백준\_donstructive (30618)

### 💡 Idea

배열의 가운데에 있을수록 점수계산에서 누적이 더 많이 되므로 배열의 가운데에 큰 숫자를 차례대로 배치해주면 된다.

예를 들어 n=5 일 때,

가장 가운데에 5 를 배치 : \_ _ 5 _ _
오른쪽에 4를 배치 : _ _ 5 4 _
왼쪽 대칭 부분에 3을 배치 : _ 3 5 4 _
다시 오른쪽에 2를 배치 : \_ 3 5 4 2
왼쪽 대칭 부분에 1을 배치 : 1 3 5 4 2

위 로직을 코드로 옮겨주면 된다.

n 이 짝수 와 홀수 일때 경우를 나눴다.

### 🧑🏻‍💻 Code

```python
n = int(input())

lst = [0] * n

if n % 2 == 0:  # 짝수일때
    temp = n
    for i in range(n // 2, n):
        lst[i] = temp  # 오른쪽 대칭 부분
        temp -= 1

        lst[n - 1 - i] = temp  # 왼쪽 대칭 부분
        temp -= 1
else:  # 홀수일 때
    temp = n
    lst[n // 2] = temp  # 정중앙 값 채우기
    temp -= 1

    for i in range(n // 2 + 1, n):
        lst[i] = temp  # 오른쪽 대칭 부분
        temp -= 1

        lst[n - 1 - i] = temp  # 왼쪽 대칭 부분
        temp -= 1

print(*lst)

```

## 3. 프로그래머스\_파괴되지 않은 건물 (64602)

### 💡 Idea

모든 육지지점마다 bfs 를 돌린 다음, 가장 긴 거리를 리턴하면 됐다.
각 육지지점마다 visited 배열을 초기화해야함에 주의

### 🧑🏻‍💻 Code

```python
from collections import deque


def bfs(start, map, visited):
    queue = deque([(start, 0)])  # 큐를 이용하여 BFS 수행, (좌표, 거리) 형태로 저장
    visited[start[0]][start[1]] = True  # 방문 여부 체크
    max_distance = 0  # 최단 거리 중 최대 거리를 저장

    while queue:
        current, distance = queue.popleft()  # 현재위치, 거리
        max_distance = max(max_distance, distance)  # 최대 거리 갱신

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = current[0] + dx, current[1] + dy  # 현재 위치에서 4방향으로 이동

            # 지도 범위 내에 있고 육지(L)이며 방문하지 않았다면 큐에 추가
            if (
                0 <= nx < len(map)
                and 0 <= ny < len(map[0])
                and map[nx][ny] == "L"
                and not visited[nx][ny]
            ):
                queue.append(((nx, ny), distance + 1))  # 다음 위치와 거리를 큐에 추가
                visited[nx][ny] = True  # 방문 여부 표시

    return max_distance


def find_treasure_distance(map):
    max_distance = 0

    # 모든 육지 지점에 대해 최단 거리를 계산하고 최대 거리를 갱신
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "L":
                visited = [[False] * len(map[0]) for _ in range(len(map))]
                max_distance = max(max_distance, bfs((i, j), map, visited))

    return max_distance


rows, cols = map(int, input().split())
treasure_map = [input().strip() for _ in range(rows)]

# 보물의 최단 거리 출력
result = find_treasure_distance(treasure_map)
print(result)


```
