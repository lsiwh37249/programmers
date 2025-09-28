def solution(A, B):
    answer = 0
    if A == B:
        return answer
    for i in range(len(A)):
        #문자열 밀기
        C = A[-1] + A[0:-1]
        answer = answer + 1

        if C == B:
            break
        A = C
    if answer == len(A):
        return -1
    return answer