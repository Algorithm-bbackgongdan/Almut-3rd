# from collections import deque
import heapq

INF = 1e8

# start_node 부터 다른 node 들까지의 cost 계산, 최종 아이템 개수 update
def solution(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    # start_node distance 초기화
    distance = [INF] * n
    distance[start_node] = 0
    res = 0

    while q:
        curr, node = heapq.heappop(q)
        if distance[node] < curr:
            continue
        
        # 해당 node 에서 갈 수 있는 다른 node 확인
        for idx, next_dist in enumerate(graph[node]):
            dist = next_dist + curr
            if dist < distance[idx]:
                distance[idx] = dist
                heapq.heappush(q, (dist, idx))
    
    # cost 계산
    for i, d in enumerate(distance):
        if d <= m:
            res += node_item[i]

    return res

n, m, r = map(int, input().split())
node_item = list(map(int, input().split()))

# generate graph
# n*n dense matrix
graph = [[INF]*n for _ in range(n)]
for _ in range(r):
    n1, n2, l = map(int, input().split())
    graph[n1-1][n2-1] = l
    graph[n2-1][n1-1] = l

# 0~n 까지 다익스트라 알고리즘으로 노드까지의 cost 구하기
cost = [0]*n

for i in range(n):
    cost[i] = solution(i)

# print(cost)
print(max(cost))