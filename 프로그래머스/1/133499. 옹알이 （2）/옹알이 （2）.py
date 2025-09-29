def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        i = 0
        prev = ""      # 직전 단어
        valid = True   # 유효한지 체크
        
        while i < len(b):
            found = False
            for w in words:
                # 여기서 startswith 사용
                if b.startswith(w, i):
                    # 직전 단어와 같은지 확인
                    if prev == w:
                        valid = False
                        break
                    # 단어 소비
                    prev = w
                    i += len(w)
                    found = True
                    break
            if not found:
                valid = False
                break

        if valid:
            answer += 1
    return answer