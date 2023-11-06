import sys

read = sys.stdin.readline

n = int(read())
cost = [list(map(int, read().split())) for _ in range(n)]

R, G, B = 0, 1, 2
dp = [[0] * 3 for _ in range(n)]

dp[0] = cost[0]  # dp 초기값 설정

for level in range(1, n):
    dp[level][R] = min(dp[level - 1][G], dp[level - 1][B]) + cost[level][R]
    dp[level][G] = min(dp[level - 1][B], dp[level - 1][R]) + cost[level][G]
    dp[level][B] = min(dp[level - 1][R], dp[level - 1][G]) + cost[level][B]

print(min(dp[n - 1]))
