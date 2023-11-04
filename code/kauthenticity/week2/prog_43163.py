from collections import deque

MAX_NUM = 1000000000000

def isChangable(a, b) : 
    diff = 0
    
    for i in range(len(a)) : 
        if a[i] != b[i] : 
            diff += 1
        
        if diff == 2 :
            return False
    
    return True

def solution(begin, target, words):
    answer = MAX_NUM
    visited = {}
    
    for word in words : 
        visited[word] = False
        
    queue = deque([(begin, 0)])
    
    while queue : 
        cur, cnt = queue.popleft()
        
        if cur == target : 
            answer = cnt
            break
            
        for word in words : 
            if visited[word]:
                continue

            if isChangable(cur, word):
                queue.append((word, cnt + 1))
                visited[word] = True

    return 0 if answer == MAX_NUM else answer