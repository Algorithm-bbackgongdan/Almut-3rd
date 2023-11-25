import heapq

def solution(n, paths, gates, summits):
    INF = int(1e10)
    answer = []
    graph = [[] for _ in range(n+1)]
    summits.sort()
    for i, j, w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    isGate = [False]*(n+1)
    for i in gates:
        isGate[i] = True
    isSummit = [False]*(n+1)
    for i in summits:
        isSummit[i] = True
    
    def dijkstra(starts, summits):
        q = []
        intensity = [INF] * (n+1)
        for start in starts:
            heapq.heappush(q, (0, start))
            intensity[start] = 0
        while q:
            curr_intensity, curr = heapq.heappop(q)
            if intensity[curr] < curr_intensity: continue
            if isSummit[curr]: continue #산봉우리면 stop
            for next, cost in graph[curr]:
                if isGate[next]: continue
                if intensity[next] > max(curr_intensity, cost):
                    intensity[next] = max(curr_intensity, cost)
                    heapq.heappush(q, (intensity[next], next))
        
        answer = [INF,INF]
        for i in summits:
            if intensity[i] < answer[1]:
                answer[0] = i
                answer[1] = intensity[i]
        return answer
    
    return dijkstra(gates, summits)