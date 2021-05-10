# python3
def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    n_1 = 1
    n_2 = 0
    num_list = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            num_list.append((n_1 + n_2) % 10)
            n_2 = n_1
            n_1 = num_list[i]

    return num_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
