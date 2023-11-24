import heapq

def solution(n, paths, gates, summits):
    INF = 10000001
    answer = []
    summits = set(summits)
    gates = set(gates)

    graph = [[] for _ in range(n+1)]
    for p in paths:
        i, j, w = p
        graph[i].append([j,w])
        graph[j].append([i,w])

    cost = [INF]*(n+1)
    def dijkstra(start):
        # 시작점은 0
        cost[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, curr_node = heapq.heappop(q)

            # 도착
            if curr_node in summits:
                answer.append([curr_node, dist])
                continue

            # 이미 다른 최단 거리가 존재
            if cost[curr_node] < dist:
                continue

            # dist 계산
            for next_node, next_dist in graph[curr_node]:
                # 출발점 체크
                if next_node in gates:
                    continue
                
                # intensity update
                intensity = max(dist, next_dist)

                # 다음 노드까지의 intensity 가 더 작다 : 최단거리이다
                if cost[next_node] > intensity:
                    # intensity 저장
                    cost[next_node] = intensity
                    heapq.heappush(q, (cost[next_node], next_node))

    # gates 중 하나 -> summits 중 하나. (다른 gate 나 summit 방문하면 안 됨)
    # 모든 gates 에 대해 dijkstra 로 업데이트, 최단 거리 중 가장 긴 distance -> intensity
    for g in gates:
        dijkstra(g)

    # 가장 짧은 intensity / node 번호가 낮아야 함
    answer = sorted(answer, key=lambda x: (x[1], x[0]))
    
    return answer[0]

# [5, 3]
print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))

# [3, 4]
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))

# [5, 1]
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))

# [5, 6]
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))