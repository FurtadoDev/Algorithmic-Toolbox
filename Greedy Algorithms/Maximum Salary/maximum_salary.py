# python3
from itertools import permutations
from functools import cmp_to_key


def mycmp(a, b):
    lhs = int(str(a) + str(b))
    rhs = int(str(b) + str(a))
    if lhs > rhs:
        return 1
    elif lhs < rhs:
        return -1
    else:
        return 0


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    sorted_numbers = sorted(numbers, key=cmp_to_key(mycmp), reverse=True)
    answer = int(''.join(str(x) for x in sorted_numbers))
    return answer


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
