import heapq
from math import inf

def solution(n, paths, gates, summits):
    # 간선 정리 (양방향)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    # 산봉우리 판별
    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    # gates 모두 시작 위치
    distance = [inf] * (n + 1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])

    # 다익스트라
    while queue:
        d, i = heapq.heappop(queue)
        # 산봉우리면 바로 continue
        # 이렇게 해야 두 개 이상의 산봉우리를 방문하지 않는다.
        if distance[i] < d or is_summit[i]:
            continue
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])

    # 결과
    # 거리가 같으면 산봉우리의 번호가 작은 것을 출력해야 하므로
    # 산봉우리를 정렬하여 살펴보자.
    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result