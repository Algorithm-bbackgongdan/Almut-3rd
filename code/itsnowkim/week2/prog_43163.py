from collections import deque

def check(curr, item):
    count = 0
    
    for i in range(len(curr)):
        if curr[i] != item[i]:
            count+=1
            if count > 1:
                return False
    
    return True

def solution(begin, target, words):
    answer = 0
    # 최단경로 문제와 동일하게 풀이 가능
    
    # 만약 target 이 words 에 없는 경우에는 바로 0 return
    if target not in words:
        return 0
    
    # bfs 로 찾고, 찾은 순간 answer 출력
    q = deque()
    q.append((begin, 0))
    
    while q:
        temp = []
        curr, count = q.popleft()

        if curr == target:
            break
        
        # curr 기준으로 한 글자 다른 word 추가
        for item in words:
            if check(curr, item):
                temp.append(item)
        
        # temp 에 있는 word queue 에 추가, words 에서 제거
        for item in temp:
            q.append((item, count+1))
            words.remove(item)

    return count


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))