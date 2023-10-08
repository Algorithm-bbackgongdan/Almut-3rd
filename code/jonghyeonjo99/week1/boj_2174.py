A, B = map(int,input().split())
N, M = map(int,input().split())

robots = []

# N W S E
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(1,N+1):

  robot = list(input().split())

  #문제의 좌표 변환
  x = B - int(robot[1])
  y = int(robot[0]) - 1
  robot[0] = x
  robot[1] = y

  if robot[2] == 'N':
    robot[2] = 0
  elif robot[2] == 'W':
    robot[2] = 1
  elif robot[2] == 'S':
    robot[2] = 2
  else:           #'E'
    robot[2] = 3

  robots.append(robot)

for i in range(M):
  order = list(input().split())
  for j in range(int(order[2])):
    if order[1] == 'F':
      nx = robots[int(order[0])-1][0] + dx[robots[int(order[0])-1][2]]
      ny = robots[int(order[0])-1][1] + dy[robots[int(order[0])-1][2]]
      for k in robots:
        if k[0] == nx and k[1] == ny:
          print("Robot",order[0],"crashes into robot",robots.index(k)+1)
          exit()
      robots[int(order[0])-1][0] = nx
      robots[int(order[0])-1][1] = ny

      if nx < 0 or nx >= B or ny < 0 or ny >= A:
        print("Robot",order[0],"crashes into the wall")
        exit()
    elif order[1] == 'L':
      #robot 머리 숫자 + 1
      #if robot 머리 숫자 == 4 -> 0으로 바꿈
      robots[int(order[0])-1][2] += 1
      if robots[int(order[0])-1][2] == 4:
        robots[int(order[0])-1][2] = 0
    elif order[1] == 'R':
      #robot 머리 숫자 - 1
      #if robot 머리 숫자 == -1 -> 3으로 바꿈
      robots[int(order[0])-1][2] -= 1
      if robots[int(order[0])-1][2] == -1:
        robots[int(order[0])-1][2] = 3
print("OK")


