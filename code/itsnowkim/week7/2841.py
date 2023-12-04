n, p = map(int, input().split())
answer = 0
line = [[] for _ in range(7)]

for _ in range(n):
    l, p = map(int, input().split())

    # l 에 p 보다 큰 수로 누르고 있을 경우 해당 손가락 떼야 함
    # 더 작은 수로 누르고 있을 경우 추가로 누르면 됨
    while True:
        if len(line[l])==0 or line[l][0] < p:
            answer += 1
            line[l] = [p] + line[l]
            break
        if line[l][0] > p:
            answer += 1
            line[l] = line[l][1:]
        else:
            break

print(answer)

            
                

