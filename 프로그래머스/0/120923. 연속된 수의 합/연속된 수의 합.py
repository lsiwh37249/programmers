def solution(num, total):
    answer = []
    mid = int(total / num)
    start = mid - int(num/2)
    print(mid,start)
    if total % num ==0:
        for i in range(start,start+num,1):
            answer.append(i)
    else:
        for i in range(start+1, start+num+1,1):
            answer.append(i)
    print(answer)
            
        
    return answer