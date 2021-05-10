# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    f_i_1 = 1
    f_i_2 = 0

    if n == 0:
        last_digit_of_sum = 0
    elif n == 1:
        last_digit_of_sum = 1
    else:
        f_i = 1
        last_digit_of_sum = 1
        for i in range(2, n+1):
            f_i = (f_i_1 + f_i_2) % 10
            last_digit_of_sum = (last_digit_of_sum + f_i) % 10
            f_i_2 = f_i_1
            f_i_1 = f_i

    return last_digit_of_sum


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
