def solution(chicken):
    answer = 0
    coupon = chicken 
    while coupon >= 10:
        t_c = coupon // 10 
        r_c = coupon % 10 
        answer = answer + t_c
        coupon = t_c + r_c
    return answer