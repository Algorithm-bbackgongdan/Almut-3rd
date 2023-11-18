N = int(input())
A = list(map(int, input().split()))
M = int(input())
queries = [list(map(int, input().split())) for _ in range(M)]

# 각 사람이 몇 번 집인지 dict로 저장
dic = {}
for i in range(N):
    dic[A[i]] = i + 1

for query in queries:
    houses = []
    A_copy = A[:]
    for j in range(query[0], query[1] + 1):
        houses.append(dic[j])
    houses.sort()

    people = list(range(query[0], query[1] + 1))

    for i in range(len(houses)):
        A_copy[houses[i] - 1] = people[i]

    print(*A_copy)
