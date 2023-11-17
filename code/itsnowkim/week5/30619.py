import copy

def sol(l, r):
    # l 부터 r 까지 순서대로 넣을 수 있는 자리에 넣으면 그게 ans 가 됨.
    rearange = [x for x in range(l, r+1)]
    p = 0
    answer = copy.deepcopy(arr)

    for idx, person in enumerate(answer):
        if person >= l and person <= r:
            answer[idx] = rearange[p]
            p+=1

    return answer

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    L, R = map(int, input().split())
    answer = sol(L, R)
    
    # print ans
    for i in answer:
        print(i, end=' ')
    print('')