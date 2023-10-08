n = int(input())
honeys = list(map(int,input().split()))
result = 0

prefixSum = [0] * n
prefixSum[0] = honeys[0]
for i in range(1, n):
  prefixSum[i] = prefixSum[i-1] + honeys[i]

if n == 3:
  result = max(honeys) * 2

#꿀통 맨 왼쪽
for i in range(1, n-1):
  result = max(result, prefixSum[n-2] + prefixSum[i] - 2 * honeys[i])

#꿀통 맨 오른쪽
for i in range(1, n-1):
  result = max(result, prefixSum[n-1] - honeys[0] - honeys[i] + prefixSum[n-1] - prefixSum[i])

#꿀통 가운데
for i in range(1, n-1):
  result = max(result, prefixSum[i] - honeys[0] + prefixSum[n-2] - prefixSum[i-1])

print(result)