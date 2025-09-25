def solution(s):
    answer = []
    s = s.split(" ")
    for word in s:
        for i in range(len(word)):
            if word[i].isalpha() != True:
                temp = word[i]
                answer.append(temp)
                continue
            if i==0 :
                temp = word[i]
                temp = temp.upper()
                answer.append(temp)
            else:
                temp = word[i]
                temp = temp.lower()
                answer.append(temp)
        answer.append(" ")
    answer = "".join(answer[:-1])
    return answer