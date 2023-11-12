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
