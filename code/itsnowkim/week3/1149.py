"""
min_cost(N) = min(N_min(R), N_min(G), N_min(B))
N_min(R) = min(N-1_min(G)+N(R), N-1_min(B)+N(R))
"""

N = int(input())
input_map = [list(map(int, input().split())) for _ in range(N)]

cost_R = [0]*N
cost_G = [0]*N
cost_B = [0]*N
cost = [0]*N

cost_R[0] = input_map[0][0]
cost_G[0] = input_map[0][1]
cost_B[0] = input_map[0][2]
cost[0] = min(cost_R[0],cost_G[0],cost_B[0])

for i in range(1, N):
    cost_R[i] = min(cost_B[i-1] + input_map[i][0], cost_G[i-1] + input_map[i][0])
    cost_G[i] = min(cost_B[i-1] + input_map[i][1], cost_R[i-1] + input_map[i][1])
    cost_B[i] = min(cost_R[i-1] + input_map[i][2], cost_G[i-1] + input_map[i][2])

    cost[i] = min(cost_R[i], cost_G[i], cost_B[i])

print(cost[-1])
