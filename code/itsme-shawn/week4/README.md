# 2주차

## 1. 백준\_서강그라운드 (14938)

### 💡 Idea

`한 노드로부터 다른 노드까지의 최단거리 <= 수색거리` : **아이템 획득 가능**

따라서 노드 개수만큼 반복문을 돌면서 각 노드에서 다익스트라 알고리즘을 적용하면

각 노드에서의 다른 노드까지의 최단거리 정보를 얻을 수 있다.

각 노드에서 획득할 수 있는 아이템의 개수를 저장한다.

최종적으로 아이템을 가장 많이 획득할 수 있는 노드의 아이템 획득 개수가 정답이 된다.

### 🧑🏻‍💻 Code

```python
import heapq as hq
import sys

n, m, r = map(int, sys.stdin.readline().split())

items = list(map(int, sys.stdin.readline().split()))
items.insert(0, 0)

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

MAX = int(1e9)
distance = [MAX] * (n + 1)

result = [0] * (n + 1)


def dijkstra(start):
    q = []

    distance[start] = 0  # 시작점 세팅
    hq.heappush(q, (0, start))  # 힙에 시작점 push

    while q:
        dist, cur = hq.heappop(q)

        if dist <= distance[cur]:  # 현재 노드까지의 거리가 기존에 저장된 거리보다 작으면
            for nxt, cost in graph[cur]:
                nxt_dist = dist + cost  # 다음 노드까지의 거리 계산
                if nxt_dist < distance[nxt]:
                    distance[nxt] = nxt_dist  # 다음 노드까지의 거리가 기존에 저장된 거리보다 작으면 갱신
                    hq.heappush(q, (nxt_dist, nxt))


for i in range(1, n + 1):
    distance = [MAX] * (n + 1)
    dijkstra(i)
    tmp = 0
    for j in range(1, n + 1):
        if distance[j] <= m:
            tmp += items[j]
    result[i] = tmp

print(max(result))


```

## 2. 백준\_특정한 최단경로 (1504)

### 💡 Idea

반드시 거쳐야 하는 노드를 v1,v2 라고 하면,

- 경우 1 : 1번노드 -> v1노드 -> v2노드 -> n번노드 순 방문
  => `1번노드 ~ v1노드 의 최단거리` + `v1노드 ~ v2노드 의 최단거리` + `v2노드 ~ n번노드 의 최단거리`
- 경우 2 : 1번노드 -> v2노드 -> v1노드 -> n번노드 순 방문
  => `1번노드 ~ v2노드 의 최단거리` + `v2노드 ~ v1노드 의 최단거리` + `v1노드 ~ n번노드 의 최단거리`

다익스트라를 통해 최단거리를 구한 후 경우1 과 경우2 를 비교해서 더 작은 값이 정답이 된다.

(python3 로 제출하니 시간초과가 발생해서 pypy 로 제출했더니 통과했다.)

### 🧑🏻‍💻 Code

```python
import heapq
import sys


def dijkstra(start, graph):
    n = len(graph)
    distance = [float("inf")] * n
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, cur = heapq.heappop(heap)

        if dist > distance[cur]:
            continue

        for nxt, cost in graph[cur]:
            nxt_dist = dist + cost
            if nxt_dist < distance[nxt]:
                distance[nxt] = nxt_dist
                heapq.heappush(heap, (nxt_dist, nxt))

    return distance


def find_shortest_path(graph, v1, v2):
    n = len(graph)

    # 1번 정점에서 v1 정점을 거쳐 v2 정점까지의 최단 경로
    dist_1_to_v1 = dijkstra(1, graph)
    dist_v1_to_v2 = dijkstra(v1, graph)
    dist_v2_to_N = dijkstra(v2, graph)

    path1 = dist_1_to_v1[v1] + dist_v1_to_v2[v2] + dist_v2_to_N[-1]

    # 1번 정점에서 v2 정점을 거쳐 v1 정점까지의 최단 경로
    dist_1_to_v2 = dijkstra(1, graph)
    dist_v2_to_v1 = dijkstra(v2, graph)
    dist_v1_to_N = dijkstra(v1, graph)

    path2 = dist_1_to_v2[v2] + dist_v2_to_v1[v1] + dist_v1_to_N[-1]

    # 두 경로 중 최소값을 선택
    result = min(path1, path2)

    return result


# 입력 처리
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 결과 출력
result = find_shortest_path(graph, v1, v2)
print(result if result != float("inf") else -1)


```

## 3. 프로그래머스\_파괴되지 않은 건물 (64602)

### 💡 Idea

> 최초 아이디어 (시간초과)

- 스킬배열을 순회하면서 각 스킬들을 건물들에 적용
- 최종 내구도를 계산해서 건물 내구도가 1 이상인 것들만 카운트해서 리턴

=> 정확성 테스트는 통과했지만 효율성 테스트에서 모두 시간초과가 발생했다.

> 시간초과 개선

시간초과 이유 : 매 스킬마다 직접 건물 내구도를 감소시키는 과정에서 2차원배열을 순회하므로 그에 따라 O(n\*m) 이 추가적으로 발생

- 누적합을 저장하는 배열을 생성해서 누적합 정보를 저장한 다음, 최종 누적합을 계산한다.
- 최종 누적합 테이블과 원본 테이블을 합치게되면 건물의 내구도가 계산된다.
  => O(n\*m) 한 번으로만 가능

누적합 알고리즘과 코드는 아래 블로그를 참고했습니다
https://kimjingo.tistory.com/155

### 🧑🏻‍💻 Code

> 최초 코드 (시간초과)

```python
def solution(board, skill):

    n, m = len(board), len(board[0])

    # 건물 내구도
    durability = [[0] * m for _ in range(n)]

    # 초기 내구도 할당
    for i in range(n):
        for j in range(m):
            durability[i][j] = board[i][j]

    # 스킬 적용
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if type == 1:
                    durability[i][j] -= degree
                elif type == 2:
                    durability[i][j] += degree

    # 최종 내구도 계산
    count = 0
    for i in range(n):
        for j in range(m):
            if durability[i][j] > 0:
                count += 1

    return count

```

<br>

> 시간초과 개선

```python
def solution(board, skill):
    answer = 0

    n, m = len(board), len(board[0])

    # 누적합을 저장하는 2차원 배열
    temp = [[0] * (m + 1) for _ in range(n + 1)]

    # 스킬 적용
    # 누적합을 기록
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        if type == 1:
            temp[r1][c1] -= degree
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] -= degree
        elif type == 2:
            temp[r1][c1] += degree
            temp[r1][c2 + 1] -= degree
            temp[r2 + 1][c1] -= degree
            temp[r2 + 1][c2 + 1] += degree

    # 최종 누적합 계산

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            temp[i][j + 1] += temp[i][j]

    # 열 기준 누적합
    for j in range(m):
        for i in range(n):
            temp[i + 1][j] += temp[i][j]

    # 기존 배열과 합함
    for i in range(n):
        for j in range(m):
            board[i][j] += temp[i][j]

            # board에 값이 1이상인 경우 answer 증가
            if board[i][j] > 0:
                answer += 1

    return answer
```
