def solution(n, s):
    if s < n :
        return [-1]
    q = s // n
    r = s % n
    answer = [q] * (n-r) + [q+1] * r
    print(answer)
    return answer