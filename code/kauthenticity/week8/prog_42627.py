from heapq import heappush, heappop, heapify


def solution(jobs):
    answer = 0
    heap = []
    end, i = 0, 0
    start = -1
    
    while len(jobs) > i : 
        for job in jobs :
            if start < job[0] <= end : 
                heappush(heap, (job[1], job[0]))
        
        if len(heap) > 0 : 
            take, request = heappop(heap)
            
            start = end
            end += take
            answer += end - request
            i += 1
        else : 
            end += 1
    answer = answer//len(jobs)
    return answer