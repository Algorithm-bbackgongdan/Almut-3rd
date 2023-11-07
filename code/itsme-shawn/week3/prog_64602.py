def solution(stones, k):
    left, right = 1, max(stones)
    res = 0

    while left <= right:
        mid = (left + right) // 2

        consecutive_zeros = 0  # 연속된 0의 개수 초기화
        flag = True  # 건널 수 있는지 여부 플래그

        for stone in stones:
            if stone < mid:
                consecutive_zeros += 1  # 현재 돌의 값이 mid보다 작으면 연속된 0의 개수를 증가
                if consecutive_zeros >= k:
                    flag = False  # 연속된 0의 개수가 k보다 크거나 같으면 건널 수 없음
                    break
            else:
                consecutive_zeros = 0  # 현재 돌의 값이 mid 이상이면 연속된 0의 개수 초기화

        if flag:
            res = mid  # 답 저장
            left = mid + 1  # 건널 수 있는 경우, 왼쪽 범위를 mid + 1로 이동
        else:
            right = mid - 1  # 건널 수 없는 경우, 오른쪽 범위를 mid - 1로 이동

    return res
