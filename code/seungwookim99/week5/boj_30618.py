import sys

N = int(sys.stdin.readline().rstrip())
P = [0]*(N+1)
for i in range(1,N+1):
  if i % 2 == 1:
    P[i//2 + 1] = i
  else:
    P[N-i//2 + 1] = i

for e in P[1:]:
  print(e, end=" ")
