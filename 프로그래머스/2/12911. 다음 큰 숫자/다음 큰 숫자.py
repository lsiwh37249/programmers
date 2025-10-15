def solution(n):
    answer = 0
    n_s = 0 
    l_n = list(str(bin(n)[2:]))
    for k in l_n:
        n_s = n_s + int(k)
        
    for i in range(n+1,1000004):
        b = bin(i)[2:]
        l_i = list(str(b))
        s = 0
        for j in l_i:
            s = s + int(j) 
        if n_s == s:
            answer = i
            break
    return answer