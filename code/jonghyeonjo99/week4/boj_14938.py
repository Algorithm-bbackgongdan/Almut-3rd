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