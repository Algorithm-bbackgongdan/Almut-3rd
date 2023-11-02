from sys import stdin
def solution():
    global n, numbers

    answer = []
    low, high = 0, n - 1
    minVal = float('inf')

    numbers.sort()

    while low < high:
        if abs(numbers[low] + numbers[high]) < minVal:
            minVal = abs(numbers[low] + numbers[high])
            answer = [numbers[low], numbers[high]]

            if minVal == 0:
                break

        if numbers[low] + numbers[high] < 0:
            low += 1
        elif numbers[low] + numbers[high] > 0:
            high -= 1

    return answer


n = int(input())
numbers = list(map(int, stdin.readline().rstrip().split()))
a, b = solution()
print(a, b)
