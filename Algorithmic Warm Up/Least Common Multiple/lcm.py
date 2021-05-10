# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if a == 0 and b == 0:
        return 0
    if a == 0 and b > 0:
        return b
    if a > 0 and b == 0:
        return a

    greater = max(a, b)
    lesser = min(a, b)
    remainder = greater % lesser
    return gcd(lesser, remainder)


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    gcd_a_b = gcd(a, b)
    lcm_a_b = (a*b)/gcd_a_b
    return lcm_a_b


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
