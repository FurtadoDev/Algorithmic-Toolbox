# python3

def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    num_list = [0, 1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            num_list.append(num_list[i-1] + num_list[i-2])

    return num_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
