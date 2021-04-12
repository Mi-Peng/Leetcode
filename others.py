# 最大公约数 最小公倍数
# 暴力
def gcd_lcm(a, b):
    min_num = min([a, b])
    while True:
        if (a % min_num == 0) and (b % min_num == 0):
            break
        min_num -= 1
    gcd = min_num

    max_num = max([a, b])
    while True:
        if (max_num % a == 0) and (max_num % b == 0):
            break
        max_num += 1
    lcm = max_num
    return gcd, lcm


print(gcd_lcm(12, 18))


# 欧几里得法/辗转相除法
def gcd_lcm(a, b):
    # gcd
    ai, bi = max([a, b]), min([a, b])
    while ai % bi != 0:
        ai, bi = bi, ai % bi
    gcd = bi
    # lcm
    lcm = a * b / gcd
    return gcd, lcm

print(gcd_lcm(12, 18))