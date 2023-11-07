def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while(left <= right):
        cnt = 0
        results = []
        mid = (left + right) // 2

        for i in range(len(stones)):
            if stones[i] <= mid:
                cnt += 1
            else:
                results.append(cnt)
                cnt = 0
                
        results.append(cnt)
        result = max(results)

        if result < k:
            left = mid + 1

        else:
            answer = mid
            right = mid -1
    return answer