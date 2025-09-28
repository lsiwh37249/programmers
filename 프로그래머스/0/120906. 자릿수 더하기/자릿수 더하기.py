def solution(n):
    answer = 0
    my_list = list(str(n))
    for c in my_list: 
        answer = answer + int(c)
    return answer