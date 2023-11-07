n = int(input())

houses = []
dp = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
  house = list(map(int,input().split()))
  houses.append(house)

dp[0][0] = houses[0][0]
dp[0][1] = houses[0][1]
dp[0][2] = houses[0][2]

for i in range(1,n):
  dp[i][0] = min(houses[i][0] + dp[i-1][1],houses[i][0] + dp[i-1][2])
  dp[i][1] = min(houses[i][1] + dp[i-1][0], houses[i][1] + dp[i-1][2])
  dp[i][2] = min(houses[i][2] + dp[i-1][0], houses[i][2] + dp[i-1][1])

result = min(dp[n-1])
print(result)

