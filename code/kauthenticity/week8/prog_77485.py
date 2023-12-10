def setNumbers(matrix, query, numbers):
    minNum = 10001
    
    
    x1, y1, x2, y2 = query
    
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    idx = 0
    
    
    for i in range(y1, y2+1) : 
        matrix[x1][i] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1
        
    for i in range(x1+1, x2+1) : 
        matrix[i][y2] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1
        
    for i in range(y2-1, y1-1, -1) :
        matrix[x2][i] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1
        
        
    for i in range(x2-1, x1, -1):
        matrix[i][y1] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1
        
    return minNum
    

def getNumbers(matrix, query) : 
    x1, y1, x2, y2 = query
    numbers = []
    
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    
    for i in range(y1, y2+1) : 
        numbers.append(matrix[x1][i])
        
    for i in range(x1+1, x2+1) : 
        numbers.append(matrix[i][y2])
        
    for i in range(y2-1, y1-1, -1) :
        numbers.append(matrix[x2][i])
        
    for i in range(x2-1, x1, -1):
        numbers.append(matrix[i][y1])
        
    return numbers
    

def move(matrix, query):    
    numbers = getNumbers(matrix, query)
    
    last = numbers[-1]
    numbers = [last] + numbers[0:-1]
    
    minNum = setNumbers(matrix, query, numbers)
    
    
    return minNum

def solution(rows, columns, queries):
    answer = []

    matrix = []

    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(i * columns + j + 1)
    for query in queries:
        answer.append(move(matrix, query))
        
    return answer