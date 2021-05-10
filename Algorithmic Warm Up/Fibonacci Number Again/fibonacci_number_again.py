# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def get_period(m):
    assert 2 <= m <= 10 ** 3
    found = False
    f_i_2 = 0
    f_i_1 = 1
    f_i = 0
    r_prev = 1
    r_current = 0  # initialize to zero for start
    i = 2
    while not found:
        f_i = f_i_1 + f_i_2
        r_current = f_i % m
        if r_prev == 0 and r_current == 1:
            found = True
        else:
            f_i_2 = f_i_1
            f_i_1 = f_i
            r_prev = r_current
            i = i + 1
    return (i - 2) + 1


def fibonacci_number(n):
    num_list = [0, 1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            num_list.append(num_list[i-1] + num_list[i-2])

    return num_list[n]


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    # get pisano period
    period = get_period(m)
    r = n % period
    return fibonacci_number(r) % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
    # print(get_period(input_m))
