from sys import stdin

n = int(stdin.readline())
solutions = list(map(int,stdin.readline().split()))

solutions.sort()

start = 0
end = n - 1
result = 100000000000

while start < end:

  temp = solutions[start] + solutions[end]

  if abs(temp) < result:
    result = abs(temp)
    left = start
    right = end
  
  if temp == 0:
    break
  elif temp > 0:
    end -= 1
  else:
    start += 1

print(solutions[left], solutions[right])