# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    period_length = 60
    final_sum = 0

    if from_index == to_index:
        return last_digit_of_fibonacci_number(from_index)
    else:
        # ignore the 0th index
        new_start = from_index + 1
        new_end = to_index + 1

        subtract_first_n = 0
        # offset new_start to the start of the period
        offset_start = 0
        if new_start == 1:
            offset_start = 1
            subtract_first_n = 0
        else:
            offset_start = new_start - ((new_start % period_length) - 1)
            subtract_first_n = (new_start % period_length) - 1

        # offset to_index to the end of the period
        offset_end = 0
        if(new_end % period_length) == 0:
            offset_end = new_end
        else:
            offset_end = new_end + (period_length - (new_end % period_length))

        num_periods_after_offset = int((offset_end - (offset_start - 1)) / period_length)
        add_first_n = 0
        if num_periods_after_offset == 1:
            num_periods = num_periods_after_offset
            if from_index == 0:
                final_sum = last_digit_of_the_sum_of_fibonacci_numbers(new_end - 1)
            else:
                final_sum = last_digit_of_the_sum_of_fibonacci_numbers(new_end - 1)
                if last_digit_of_the_sum_of_fibonacci_numbers(subtract_first_n - 1) > final_sum:
                    final_sum = ((10 + final_sum) - last_digit_of_the_sum_of_fibonacci_numbers(subtract_first_n - 1)) % 10
                else:
                    final_sum = (final_sum - last_digit_of_the_sum_of_fibonacci_numbers(subtract_first_n - 1)) % 10
        else:
            # reducing the number of periods after offset by 1 so that the remainder(sum_add_first_n) can be added in easily
            if new_end % period_length == 0:
                num_periods = num_periods_after_offset
            else:
                num_periods = num_periods_after_offset - 1

            add_first_n = new_end % period_length
            sum_add_first_n = last_digit_of_the_sum_of_fibonacci_numbers(add_first_n - 1)
            sum_whole_period = last_digit_of_the_sum_of_fibonacci_numbers(period_length - 1)
            sum_subtract_first_n = last_digit_of_the_sum_of_fibonacci_numbers(subtract_first_n - 1)
            final_sum = (num_periods * sum_whole_period) % 10
            final_sum = (final_sum + sum_add_first_n) % 10
            if sum_subtract_first_n > final_sum:
                final_sum = (10 - sum_subtract_first_n) % 10
            else:
                final_sum = (final_sum - sum_subtract_first_n) % 10

    return final_sum


# pass in n where n refers to the nth fib no.
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


# pass in n where n refers to the nth fib no.
def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 18

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
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
