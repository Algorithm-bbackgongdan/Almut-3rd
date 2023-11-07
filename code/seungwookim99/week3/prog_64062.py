# Python 풀이
def canPass(num, stones, k):
    count = 0
    for i in range(len(stones)):
        if stones[i] < num:
            count += 1
        else:
            count = 0
        if count == k:
            return False
    return True


def solution(stones, k):
    answer = 0
    right, left = max(stones), min(stones)
    while left <= right:
        mid = (left + right) // 2
        if canPass(mid, stones, k):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer
