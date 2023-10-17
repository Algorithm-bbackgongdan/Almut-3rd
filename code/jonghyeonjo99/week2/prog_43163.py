from collections import deque

def solution(begin, target, words):

    answer = 0
    words.append(begin)
    
    visited = [0 for _ in range(len(words))]
    gragh = [[] for _ in range(len(words))]

    if target not in words:
        return 0

    for i in range(len(words)):
        word = words[i]
        for j in range(len(words)):
            diff = 0
            for k in range(len(word)):
                if word[k] != words[j][k]:
                    diff += 1
            if diff == 1:
                gragh[i].append(j)
    
   
    # begin
    queue = deque([len(words) -1])
    visited[len(words)-1] = 1

    while queue:
        num = queue.popleft()
        if words[num] == target:
            answer = visited[num]-1
            break

        for i in gragh[num]:
            if visited[i] == 0:
                visited[i] = visited[num] + 1
                queue.append(i)
                
    return answer
