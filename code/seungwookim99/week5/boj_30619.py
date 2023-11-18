import sys

N = int(sys.stdin.readline().rstrip())
A = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
for _ in range(M):
  L, R = map(int, sys.stdin.readline().rstrip().split())
  tmp = L
  for i in range(1,N+1):
    if L <= A[i] <= R:
      print(tmp, end=" ")
      tmp += 1
    else:
      print(A[i], end=" ")
  print()