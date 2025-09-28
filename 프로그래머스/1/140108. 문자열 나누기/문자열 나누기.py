def solution(s):
    answer = 0
    f = ""
    x, nx = 0, 0
    for i in list(s):
        # 첫번째인 경우
        if x == 0 and nx == 0:
            f = i
            x = x + 1
            continue
        else:
            if f == i:
                x = x + 1
            else:
                nx = nx + 1
                
            if x == nx :
                answer = answer + 1
                x, nx = 0,0
                continue
    if x != nx:
        answer = answer + 1 
        
    return answer