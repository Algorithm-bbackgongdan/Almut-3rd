from collections import deque

N = int(input())

# 가운데에 큰 숫자가 위치하도록 해야 함.
q = deque([N])

x = N-1
while x > 0:
    q.append(x)
    x = x-2

x = N-2
while x>0:
    q.appendleft(x)
    x = x-2

for i in q:
    print(i, end=' ')

print('')
