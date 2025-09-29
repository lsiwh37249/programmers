def solution(rsp):
    win = {
        "2" : "0",
        "5" : "2",
        "0" : "5"
    }
    l_rsp = list(rsp)
    temp = []
    for v in l_rsp:
        temp.append((win.get(v)))
    print(temp)
    answer = "".join(temp)
    return answer