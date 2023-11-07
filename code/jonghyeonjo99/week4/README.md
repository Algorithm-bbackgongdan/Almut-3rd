# boj_14938 : 서강그라운드
### code
```python
import sys
import heapq

n, m, r = map(int,sys.stdin.readline().rstrip().split())
items = list(map(int,sys.stdin.readline().rstrip().split()))

gragh = [[] for i in range(n+1)]
results = []

for _ in range(r):
  #a노드, b노드, 간선가중치 c
  a, b, c = map(int,sys.stdin.readline().rstrip().split())
  # 양방향
  gragh[a].append((b,c))
  gragh[b].append((a,c))

def dijkstra(start):
  hq = []
  heapq.heappush(hq, (0, start))
  distance[start] = 0
  while hq:
    dist, now = heapq.heappop(hq)
    if distance[now] < dist:
      continue
    for i in gragh[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(hq, (cost, i[0]))

for i in range(n):
  distance = [1e9] * (n+1)
  result = 0
  dijkstra(i)
  for j in range(1,n+1):
    if distance[j] <= m:
      result += items[j-1]
    results.append(result)

print(max(results))
  ```
## 결과
### 성공
## 접근
모든 지역에서 각각 출발 했을 때 얻을 수 있는 최대 아이템의 수를 비교해야겠다고 생각했고, 지역의 개수가 최대 100개인 것을 확인하고 시간복잡도는 무난할 것으로 예상했다.
1. 각 지역에 있는 아이템의 개수를 "items list"에 저장해둔다.
2. 각 지역의 번호, 지역과 지역사이 간선과 가중치를 "gragh"에 저장한다.
3. "gragh"를 다익스트라 알고리즘을 사용하여 각각의 지역에서 출발했을 때, 최단 거리를 구한다.
4. 출발 지역으로부터 연결된 지역까지의 최단거리가 수색범위보다 작거나 같을 때, 그 지역의 아이템 개수를 "result"에 더해 예은이가 얻을 수 있는 아이템의 개수를 저장한다.
5. result 중 가장 많은 아이템을 얻었을 때를 출력.
## 문제 회고
전형적인 다익스트라 문제라 생각했고, 어렵지않게 풀 수 있었다.

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고