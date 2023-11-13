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
