def solution(i, j, k):
    answer = 0
    for v in range(i,j+1):
        for i in list(str(v)):
            if str(k)==i:
                answer = answer + 1
    return answer