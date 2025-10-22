from collections import Counter
def solution(want, number, discount):
    answer = 0
    # banana : 3
    s_want = Counter({w : n for w,n in zip(want, number)})

    for i in range(len(discount) - 9):
        s_f = Counter(discount[i:i+10])
        
        if s_want == s_f:
            answer = answer + 1 
    return answer