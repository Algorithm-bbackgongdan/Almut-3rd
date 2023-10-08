# Python 풀이
import sys

N = int(sys.stdin.readline().rstrip())
place = list(map(int, sys.stdin.readline().rstrip().split()))

cumulativeSumFromLeft = [0] * N
cumulativeSumFromLeft[0] = place[0]
for i in range(1, N):
    cumulativeSumFromLeft[i] = cumulativeSumFromLeft[i - 1] + place[i]

cumulativeSumFromRight = [0] * N
cumulativeSumFromRight[N - 1] = place[N - 1]
for i in range(N - 2, -1, -1):
    cumulativeSumFromRight[i] = cumulativeSumFromRight[i + 1] + place[i]

maxVal = 0
# 벌통이 맨 왼쪽일 경우
for i in range(1, N - 1):
    maxVal = max(
        maxVal,
        cumulativeSumFromLeft[i]
        + cumulativeSumFromLeft[N - 1]
        - place[N - 1]
        - 2 * place[i],
    )

# 벌통이 맨 오른쪽일 경우
for i in range(1, N - 1):
    maxVal = max(
        maxVal,
        cumulativeSumFromRight[i] + cumulativeSumFromRight[0] - place[0] - 2 * place[i],
    )

# 벌통이 중간일 경우
for i in range(1, N - 1):
    maxVal = max(
        maxVal,
        cumulativeSumFromLeft[i] + cumulativeSumFromRight[i] - place[0] - place[N - 1],
    )
print(maxVal)
