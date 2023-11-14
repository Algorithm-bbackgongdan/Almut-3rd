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