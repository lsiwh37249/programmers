from itertools import combinations

def solution(relation):
    n_cols = len(relation[0])   # 속성 개수
    n_rows = len(relation)      # 튜플 개수
    candidate_keys = []

    for r in range(1, n_cols+1):   # 1개부터 n개까지 조합
        for comb in combinations(range(n_cols), r):
            # 해당 조합으로 projection
            projection = [tuple([row[i] for i in comb]) for row in relation]
            
            # 유일성 확인
            if len(set(projection)) == n_rows:
                # 최소성 확인
                if not any(set(key).issubset(set(comb)) for key in candidate_keys):
                    candidate_keys.append(comb)

    return len(candidate_keys)