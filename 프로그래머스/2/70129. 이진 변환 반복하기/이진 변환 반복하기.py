def solution(s):
    depth = 0
    z_count = 0
    
    while s != "1":
        z_count += s.count("0")
        s = bin(len(s.replace("0", "")))[2:]
        depth += 1

    return [depth, z_count]