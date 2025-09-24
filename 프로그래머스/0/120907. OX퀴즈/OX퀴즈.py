def solution(quiz):
    queue = []
    for q in quiz:
        answer = 0
        left, right = q.split(" = ")
        x,s,y = left.split(" ")
        if s == "+":
            answer = int(x) + int(y)
        else:
            answer = int(x) - int(y)
        
        if answer == int(right):
            queue.append("O")
        else:
            queue.append("X")
    return queue