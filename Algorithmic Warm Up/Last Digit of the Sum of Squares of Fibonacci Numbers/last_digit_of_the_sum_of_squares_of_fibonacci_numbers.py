# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    new_start = 1
    new_end = n + 1
    period_length = 60
    sum_of_whole_period = driver_code(period_length - 1)
    num_periods = 0
    final_sum = 0
    if new_end < period_length:
        num_periods = 1
        # compute the sum for the first new_end - 1 nos
        final_sum = driver_code(new_end - 1)
    else:
        remainder = new_end % period_length
        if remainder == 0:
            # just compute the sum for num_periods
            num_periods = int(new_end/period_length)
            final_sum = (num_periods * sum_of_whole_period) % 10
        else:
            # compute the sum for the first num_periods-1 and add in the sum for remainder
            num_periods = int(new_end/period_length) - 1
            sum_of_remainder = driver_code(remainder - 1)
            final_sum = (((num_periods * sum_of_whole_period) % 10) + sum_of_remainder) % 10

    return final_sum


# pass in n where n refers to the nth fib no.
def driver_code(n):
    assert 0 <= n <= 10 ** 18

    f_i_1 = 1 ** 2
    f_i_2 = 0 ** 2

    if n == 0:
        last_digit_of_sum_of_squares = 0 ** 2
    elif n == 1:
        last_digit_of_sum_of_squares = 1 ** 2
    else:
        # print(f_i_2)
        # print(f_i_1)
        f_i = 0
        last_digit_of_sum_of_squares = 1 ** 2
        for i in range(2, n+1):
            f_i = (f_i_1 + f_i_2) % 10
            # print(f_i)
            last_digit_of_sum_of_squares = (last_digit_of_sum_of_squares + (f_i ** 2)) % 10
            f_i_2 = f_i_1
            f_i_1 = f_i

    return last_digit_of_sum_of_squares


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
    # print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(input_n))
