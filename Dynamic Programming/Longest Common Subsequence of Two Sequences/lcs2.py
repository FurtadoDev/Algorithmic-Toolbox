# python3
import numpy as np


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    len_first_seq = len(first_sequence)
    len_second_seq = len(second_sequence)
    matrix = np.zeros((len_first_seq + 1, len_second_seq + 1), dtype=int)
    for r in range(1, len_first_seq + 1):
        for c in range(1, len_second_seq + 1):
            if first_sequence[r - 1] == second_sequence[c - 1]:
                matrix[r][c] = 1 + matrix[r - 1][c - 1]
            else:
                matrix[r][c] = max(matrix[r - 1][c], matrix[r][c - 1])
    # print(matrix)
    return matrix[len_first_seq][len_second_seq]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
    # a = ("G", "X", "T", "X", "A", "Y", "B")
    # b = ("A", "G", "G", "T", "A", "B")
    # print(lcs2(a, b))
