def solution(s):
    answer = []
    depth = 0
    z_count = 0
    while True:
        before_s = len(s)
        after_s = len(s.replace("0",""))
        z_count = z_count + (before_s - after_s)
        depth = depth + 1
        s = bin(after_s)[2:]
        if s == "1":
            break
    
    return [depth, z_count]