from itertools import combinations, product

def bin_search(my_list, value):
    left = 0
    right = len(my_list)

    while left < right:
        mid = (left + right) // 2

        if my_list[mid] < value:
            left = mid + 1
        else:
            right = mid

    return left


def solution(dice):

    n = len(dice)
    max_win = 0
    answer = []

    for A in combinations(range(n), n//2):

        B = [i for i in range(n) if i not in A]

        A_dice = [dice[i] for i in A]
        B_dice = [dice[i] for i in B]

        A_sum = [sum(p) for p in product(*A_dice)]
        B_sum = [sum(p) for p in product(*B_dice)]

        B_sum.sort()

        win = 0

        for a in A_sum:
            win += bin_search(B_sum, a)

        if win > max_win:
            max_win = win
            answer = A

    return [i+1 for i in answer]