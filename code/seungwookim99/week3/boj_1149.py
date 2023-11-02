# 백준 1149 : RGB거리
# Python 풀이
import sys

R, G, B = 0, 1, 2

N = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

DP = [[0] * 3 for _ in range(N)]
DP[0][R] = costs[0][R]
DP[0][G] = costs[0][G]
DP[0][B] = costs[0][B]

for i in range(1, N):
    DP[i][R] = min(DP[i - 1][G], DP[i - 1][B]) + costs[i][R]
    DP[i][G] = min(DP[i - 1][R], DP[i - 1][B]) + costs[i][G]
    DP[i][B] = min(DP[i - 1][R], DP[i - 1][G]) + costs[i][B]

print(min(DP[-1]))
