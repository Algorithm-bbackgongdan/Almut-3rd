def solution(stones, k):
    answer = 0
    start = 0
    end = max(stones)

    while start <= end:
        mid = (end + start) // 2
        flag = 0
        check = 0
        for item in stones:
            if item < mid:
                check += 1

                if check == k: # 못건넘
                    end = mid-1
                    flag = 1
                    break
            else:
                check=0
        
        if flag == 0:
            start = mid+1
            answer = mid

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3
# print(solution([7, 2, 8, 7, 2, 5, 9], 3)) # 7


