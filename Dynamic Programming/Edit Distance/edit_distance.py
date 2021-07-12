# python3
import numpy as np


def edit_distance(first_string, second_string):
    # Let the first_string be the source string and the second_string be the destination string
    # Let the rows of the matrix starting from index 1 represent the source string
    # Let the columns of the matrix starting from index 1 represent the destination string
    length_first_string = len(first_string)
    length_second_string = len(second_string)
    matrix = np.zeros((length_first_string + 1, length_second_string + 1), dtype=int)
    for r in range(0, length_first_string + 1):
        for c in range(0, length_second_string + 1):
            if r == 0 and c == 0:
                matrix[r][c] = 0
            elif r == 0 and c > 0:
                matrix[r][c] = c
            elif r > 0 and c == 0:
                matrix[r][c] = r
            else:
                if first_string[r - 1] == second_string[c - 1]:
                    matrix[r][c] = matrix[r - 1][c - 1]
                else:
                    matrix[r][c] = 1 + min(matrix[r][c - 1], matrix[r - 1][c], matrix[r - 1][c - 1])
    return matrix[length_first_string][length_second_string]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
