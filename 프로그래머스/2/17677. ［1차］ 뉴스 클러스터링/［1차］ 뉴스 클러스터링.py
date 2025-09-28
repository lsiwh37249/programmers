from collections import Counter

def solution(str1, str2):
    # 2글자씩 쪼개서 알파벳만 추출
    list1, list2 = [], []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            list1.append((str1[i] + str1[i+1]).lower())
    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            list2.append((str2[j] + str2[j+1]).lower())

    # Counter로 멀티셋 교집합/합집합 구하기
    c_list1 = Counter(list1)
    c_list2 = Counter(list2)

    con = sum((c_list1 & c_list2).values())  # 교집합 원소 수
    al = sum((c_list1 | c_list2).values())  # 합집합 원소 수

    # 자카드 유사도 계산
    if al == 0:  # 둘 다 공집합일 때
        return 65536
    return int(con / al * 65536)
