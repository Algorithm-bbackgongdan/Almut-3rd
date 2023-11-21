import sys

n = int(sys.stdin.readline().rstrip())
answer = [0 for _ in range(n+1)]

if (n % 2 == 0):
  for i in range(n//2):
    answer[i] = 2 * i + 1 #홀수
    answer[i + n//2] = n - (2*i) #짝수

else:
  for i in range(n//2+1):
    answer[i] = 2 * i + 1
    answer[i + (n//2+1)] = (n-1) - (2*i)

for i in range(len(answer) -1):
  print(answer[i], end=" ")