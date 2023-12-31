from heapq import heappush, heappop
from collections import defaultdict

def dijkstra(gates, graph, isSummit,isGate, n):
    distances = [float("inf") for _ in range(n + 1)] # distances[i]: 출발지에 상관 없이 i 로 가는 최소 intensity
    heap = []
    
    for gate in gates:
        distances[gate] = 0
        heap.append([0, gate])
    
    while heap:
        dist, cur = heappop(heap);
        
        # 이미 intensity가 최소이면 볼 필요가 없음
        # 정상 이후에는 intensity를 따지지 않아도 됨
        if dist > distances[cur] or isSummit[cur]:
            continue

        for adjacent, cost in graph[cur]:
            if isGate[adjacent]: continue # 출입구에 대해서는 intensity를 구할 필요 없음
            
            curPathCost = max(distances[cur], cost)
            if curPathCost < distances[adjacent]:
                distances[adjacent] = curPathCost
                heappush(heap, [curPathCost, adjacent])

    return distances

def solution(n, paths, gates, summits):
    answer = [-1, float("inf")]
    graph = defaultdict(list)
    isSummit = [False for _ in range(n + 1)]
    isGate = [False for _ in range(n + 1)]
    
    
    for summit in summits:
        isSummit[summit] = True;
    for gate in gates:
        isGate[gate] = True;
        
    for i, j, w in paths:
        graph[i].append([j, w]);
        graph[j].append([i, w])
    
    distances = dijkstra(gates, graph, isSummit, isGate, n)
        
    for summit in sorted(summits):
        if distances[summit] < answer[1]:
            answer = [summit, distances[summit]]
        
    return answer