# python3
import numpy as np


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    len_first_seq = len(first_sequence)
    len_second_seq = len(second_sequence)
    len_third_seq = len(third_sequence)
    matrix = np.zeros((len_first_seq + 1, len_second_seq + 1, len_third_seq + 1), dtype=int)

    for r in range(1, len_first_seq + 1):
        for c in range(1, len_second_seq + 1):
            for w in range(1, len_third_seq + 1):
                if first_sequence[r - 1] == second_sequence[c - 1] == third_sequence[w - 1]:
                    matrix[r][c][w] = 1 + matrix[r - 1][c - 1][w - 1]
                else:
                    matrix[r][c][w] = max(matrix[r - 1][c][w], matrix[r][c - 1][w], matrix[r][c][w - 1])

    return matrix[len_first_seq][len_second_seq][len_third_seq]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
