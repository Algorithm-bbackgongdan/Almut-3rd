import heapq

INF = 1e9
N, E = map(int, input().split())
# dense matrix
graph = [[INF]*N for _ in range(N)]

# generate matrix
for _ in range(E):
    s, e, l = map(int, input().split())
    s-=1
    e-=1
    graph[s][e] = l
    graph[e][s] = l

# u, v
u, v = map(int, input().split())
u -= 1
v -= 1 

def init(node):
    q = []
    distance = [INF] * N
    distance[node] = 0
    heapq.heappush(q, (0, node))

    return q, distance

def dijk(q, distance, node):
    while(q):
        cost, curr_node = heapq.heappop(q)
        # 종료조건
        if curr_node == node:
            break
        if distance[curr_node] < cost:
            continue

        for idx, len in enumerate(graph[curr_node]):
            dist = cost + len
            if dist < distance[idx]:
                distance[idx] = dist
                heapq.heappush(q, (dist, idx))
    
    return distance[node]

# first -> second -> goal
def calculate(first, second):
    ans = 0

    # 0 -> first
    q, distance = init(0)
    a1 = dijk(q, distance, first)
    # print("ans1 : ",a1)
    
    # first -> second
    q, distance = init(first)
    a2 = dijk(q,distance, second)
    # print("ans2 : ", a2)

    # second -> goal
    q, distance = init(second)
    a3 = dijk(q, distance, N-1)
    # print("ans3 : ", a3)

    ans = a1 + a2 + a3
    return ans

ans1 = calculate(u, v)
ans2 = calculate(v, u)

if ans1 >= INF and ans2 >= INF:
    print(-1)
else:
    print(min(ans1, ans2))