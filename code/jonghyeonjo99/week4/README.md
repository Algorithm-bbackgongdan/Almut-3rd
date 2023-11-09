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

# 1504 : 특정한 최단 경로
### code
```python
import sys
import heapq

n, e = map(int,sys.stdin.readline().rstrip().split())

gragh = [[] for i in range(n+1)]
distance = [1e9] * (n+1)

for i in range(e):
  a,b,c = map(int,sys.stdin.readline().rstrip().split())
  gragh[a].append((b,c))
  gragh[b].append((a,c))

v1, v2 = map(int,sys.stdin.readline().rstrip().split())

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

dijkstra(1)
start_v1 = distance[v1]
start_v2 = distance[v2]

distance = [1e9] * (n+1)
dijkstra(v1)
v1_v2 = distance[v2]
v1_end = distance[n]

distance = [1e9] * (n+1)
dijkstra(v2)
v2_end = distance[n]

result = min(start_v1 + v1_v2 + v2_end, start_v2 + v1_v2 + v1_end)

if result < 1e9:
  print(result)
else:
  print(-1)
  ```
## 결과
### 성공
## 접근
시작점부터 반드시 지나가야하는 서로다른 두 정점까지의 최단 거리를 각각 구하고, 각 정점사이 최단거리, 두번째 지나는 정점부터 n번 정점까지의 최단거리를 각각 구해서
더해준다.

무조건 1 -> v1 -> v2 -> n 순서일 필요 없음. 1 -> v2 -> v1 -> n 이 더 짧은 경로가 될 수 있다.
## 문제 회고
앞의 서강그라운드 문제와 결이 비슷하여 금방 풀 수 있었는데, 거리를 저장하는 list를 반복적으로 초기화해주는 코드가 깔끔하지않아 마음에 들지않는다.ㅜ

# prog_92344 : 파괴되지 않은 건물
### code
```python
#naive하게 짠 코드 (효율성 0점)
def solution(board, skill):
    answer = 0
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            for j in range(r1,r2+1):
                for k in range(c1,c2+1):
                    board[j][k] -= degree
        else:
            for j in range(r1,r2+1):
                for k in range(c1,c2+1):
                    board[j][k] += degree
    
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] > 0:
                answer += 1
            
    return answer

    #imos 알고리즘 이용
    def solution(board, skill):
    answer = 0
    imos = [[0 for _ in range(len(board[1]) + 1)] for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            imos[r1][c1] -= degree
            imos[r2 + 1][c1] += degree
            imos[r1][c2 + 1] += degree
            imos[r2 + 1][c2 + 1] -= degree
        else: #type == 2
            imos[r1][c1] += degree
            imos[r2 + 1][c1] -= degree
            imos[r1][c2 + 1] -= degree
            imos[r2 + 1][c2 + 1] += degree
    
    #누적합 두번
    for i in range(len(board) + 1):
        for j in range(1,len(board[1]) + 1):
            imos[i][j] += imos[i][j-1]
    
    for j in range(len(board[1]) + 1):
        for i in range(1,len(board) + 1):
            imos[i][j] += imos[i-1][j]
    
    #board에 적용
    for i in range(len(board)):
        for j in range(len(board[1])):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1
            
    return answer
  ```
## 결과
### 실패(53.8점)후 참조
## 접근
효율성은 생각하지 못하고 각각의 skill에서 board의 범위가 주어질 때마다 그 범위에 해당하는 곳에 degree만큼 연산처리를 해주었다.
skill과 board의 최대 범위를 생각하면 최대 250,000 * 1,000,000 번의 계산이 필요하기 때문에 효율성이 매우 떨어졌다.

그래서 누적합 알고리즘을 확장시킨 imos 알고리즘을 적용하여 시간복잡도를 줄일 수 있었다.
1. board보다 행과 열이 1줄씩 많은 2차원리스트를 선언한다.
2. 위에서 선언한 2차원 리스트에 skill의 결과를 저장하고자 한다.
3. skill의 행 방향 범위와 열 방향 범위의 시작과 끝을 기록한다.
4. 기록 할 때 시작은 공격이라면 -degree, 회복이라면 +degree를, 끝은 공격이라면 +degree, 회복이라면 -degree로 기록한다.
5. 이후 행 방향, 열 방향으로 각각 한번씩 누적합을 구한다.
6. board에 imos 리스트 결과를 더해 0보다 큰 즉, 파괴되지 않은 건물의 수를 구하여 return해준다.

## 문제 회고
분명 배웠던 알고리즘인데, 문제를 보고 전혀 생각이 나질 않았다.
어떤 알고리즘을 사용해야하는지 모르는 상황에서 적절한 알고리즘을 떠올리는 것이 실전에서 매우 중요하고, 그러기 위해서는 까먹지 않게 반복하는 것이 중요한 것같다...

## 참고문헌
[imos 알고리즘](https://driip.me/65d9b58c-bf02-44bf-8fba-54d394ed21e0)
