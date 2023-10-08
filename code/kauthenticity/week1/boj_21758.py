from sys import stdin
def solution(n, numbers):
    # bee1 ... bee2 ... goal
    answer = 0
    sums = [numbers[0]]

    bee1 = 0
    bee2 = 1
    goal = n - 1

    for i in range(1, n):
        sums.append(sums[i-1] + numbers[i])

    while bee2 < goal:
        answer = max(answer, sums[goal] - sums[bee1] + sums[goal] - sums[bee2] - numbers[bee2])
        bee2 += 1

    # bee1 ... goal ... bee2
    bee1 = 0
    bee2 = n - 1
    goal = 1

    while goal < bee2:
        answer = max(answer, sums[goal] - sums[bee1] + sums[bee2 - 1] - sums[goal - 1])
        goal += 1

    # goal ... bee1 ... bee2

    bee1 = n - 2
    bee2 = n - 1
    goal = 0

    while bee1 > goal:
        answer = max(answer, sums[bee1 - 1] + sums[bee2 - 1] - numbers[bee1])
        bee1 -= 1

    return answer


n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

print(solution(n, numbers))
