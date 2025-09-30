def solution(s):
    list_s = list(map(int,s.split(" ")))
    s = str(min(list_s)) + " " + str(max(list_s))
    return s