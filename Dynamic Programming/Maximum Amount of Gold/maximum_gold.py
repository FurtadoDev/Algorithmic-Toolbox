# python3

from sys import stdin
import numpy as np


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    num_rows = capacity + 1
    num_cols = len(weights) + 1
    matrix = np.zeros((num_rows, num_cols), dtype=int)
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            current_capacity = i
            current_elem_weight = weights[j - 1]
            if current_elem_weight > current_capacity:
                matrix[i][j] = matrix[i][j - 1]
            else:
                matrix[i][j] = max(matrix[i - current_elem_weight][j - 1] + current_elem_weight, matrix[i][j - 1])

    return matrix[num_rows - 1][num_cols - 1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
    # print(maximum_gold(10, (3, 5, 3, 3, 5)))
