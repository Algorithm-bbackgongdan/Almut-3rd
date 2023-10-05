# Week1
# boj_21758 : 꿀 따기
### code
```python
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

  ```
## 결과
### 성공
## 접근
가장 먼저 꿀벌 두 마리와 1개의 벌통을 무작위로 배치 후, 최대의 꿀의 양을 계산할려고 했지만,
n이 최대 100,000 이기 때문에 nC1 * (n-1)C2 이면 시간 초과가 난다고 판단 했다.

n = 3 일때는 1 개의 벌통과 꿀벌 2마리가 모두 할당되기 때문에 가장 큰 수에 벌통이 놓여있을 때 가장 많은 양의 꿀을 수확할 수 있다.

이후 n = 4, 5, 6 일 때를 하나하나 생각해보면서 공통점을 찾을 수 있었다.

벌통과 꿀벌 한 마리가 가장 멀리 떨어져 있을 때 가장 많은 양의 꿀을 수확할 수 있음을 깨달았다.
양쪽 끝 중 하나에 벌통이 있고, 반대쪽 끝에 꿀벌이 있는 경우 중, 남은 한 마리 꿀벌의 위치에 따라 가장 많은 양의 꿀을 얻을 수 있었다.

그리고 벌통이 중간 그 어딘가에 있을 때 최대로 많은 양의 꿀을 수확할 수 있는 경우가 있었는데,
이 때는 꿀벌이 양 쪽 끝에 위치함을 알 수 있었다.
## 문제 회고
벌통과 꿀벌 2마리 모두 위치를 바꿀 수 있어서 많은 경우의 수를 생각하는데 시간을 많이 소요했다.
벌통 혹은 꿀벌 중 어느 하나를 고정시키고 싶었지만 그 방법이 맞을까? 하는 생각에 많이 망설였던 문제였다. 