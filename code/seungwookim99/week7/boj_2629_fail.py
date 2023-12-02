import sys

MAX_MARBLE_WEIGHT = 40001
MAX_WEIGHT = 500

n = int(sys.stdin.readline().rstrip()) # 추 개수
weights = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip()) # 구슬 개수
marbles = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[False]*(MAX_MARBLE_WEIGHT+MAX_WEIGHT) for _ in range(n)] #(추 최대 개수 x 구슬 최대 무게)

# init dp
for i in range(n):
  dp[i][0] = True
for i in range(n):
  dp[i][weights[i]] = True

for i in range(n):
  for j in range(1, MAX_MARBLE_WEIGHT):
      # 추 안 올림
      if i > 0: dp[i][j] |= dp[i-1][j]
      # 구슬과 같은 쪽에 추 올림
      dp[i][j] |= dp[i-1][weights[i] + j]
      # 구슬과 반대 쪽에 추 올림
      dp[i][j] |= dp[i-1][abs(weights[i] - j)]


for marble in marbles:
  if dp[-1][marble]:
    print("Y", end=" ")
  else:
    print("N", end=" ")
print()