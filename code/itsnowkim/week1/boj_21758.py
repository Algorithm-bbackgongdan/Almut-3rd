def partial_sum(arr):
    # bee1's temp summation
    bee1_ans = sum(arr) - arr[0]
    ans = 0
    
    # adjust bee2
    for i in range(1, (len(arr)-1)):
        temp_ans = bee1_ans - arr[i] + sum(arr[i+1:])
        
        if temp_ans > ans:
            ans = temp_ans
    
    return ans

"""
맨 왼쪽 or 맨 오른쪽에 꿀벌과 꿀통을 놓는다.
더 작은 수가 꿀벌이 있을 위치, 같을 경우 상관 없음. 
이 때, 이 꿀벌은 전체 원소 - 본인이 위치한 원소 만큼 수확함.
다른 벌은 나머지 칸 중 한 칸에 위치하는데, for loop 돌면서 가장 좋은 output 을 가질 수 있는 칸 위에 위치하게 된다. O(N-2)
O(N)
"""
def sol1(arr):
    # initial state of index of each variables
    bee1 = 0
    
    # summation of bee1....bee2
    ans1 = partial_sum(arr)
    
    # adjust bee1
    arr = arr[::-1]

    # summation of bee1....bee2
    ans2 = partial_sum(arr)        
    
        
    return max(ans1, ans2)

"""
꿀통이 가운데 어딘가에 있는 경우 - 꿀통의 위치만 바꿔가면서 계산
O(N)
"""
def sol2(arr):
    summation = sum(arr) - arr[0] - arr[-1]
    ans = summation

    # 꿀통의 위치를 변경
    for i in range(1, (len(arr)-1)):
        if ans < summation + arr[i]:
            ans = summation + arr[i]
    return ans

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    # 꿀통이 가운데 있는 경우 - sol2 도 추가
    print(max(sol1(arr),sol2(arr)))


"""
https://www.acmicpc.net/board/view/90474
반례 : 어느 한 쪽이 크다고 무조건 그 방향으로 두 마리를 모두 날리는 것이 최적이 되지는 않습니다.
다음과 같이 왼쪽 끝이 오른쪽 끝보다 꿀이 적지만, 왼쪽 끝 바로 앞에 조금이나마 더 많은 꿀이 있는 경우를 놓칠 수 있습니다

입력
7
10 5 4 3 2 1 11

올바른 출력
48
//꿀통을 10에, 두 벌을 각각 1과 11에 놓으면 됩니다.

이 코드의 출력
42
"""