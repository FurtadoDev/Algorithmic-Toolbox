# python3
import numpy as np


def compute_min(lhs1, rhs1, lhs2, rhs2, lhs3, rhs3, lhs4, rhs4, op):
    answer1 = 0
    answer2 = 0
    answer3 = 0
    answer4 = 0
    if op == '+':
        answer1 = lhs1 + rhs1
        answer2 = lhs2 + rhs2
        answer3 = lhs3 + rhs3
        answer4 = lhs4 + rhs4
    if op == '-':
        answer1 = lhs1 - rhs1
        answer2 = lhs2 - rhs2
        answer3 = lhs3 - rhs3
        answer4 = lhs4 - rhs4
    if op == '*':
        answer1 = lhs1 * rhs1
        answer2 = lhs2 * rhs2
        answer3 = lhs3 * rhs3
        answer4 = lhs4 * rhs4

    return min(answer1, answer2, answer3, answer4)


def compute_max(lhs1, rhs1, lhs2, rhs2, lhs3, rhs3, lhs4, rhs4, op):
    answer1 = 0
    answer2 = 0
    answer3 = 0
    answer4 = 0
    if op == '+':
        answer1 = lhs1 + rhs1
        answer2 = lhs2 + rhs2
        answer3 = lhs3 + rhs3
        answer4 = lhs4 + rhs4
    if op == '-':
        answer1 = lhs1 - rhs1
        answer2 = lhs2 - rhs2
        answer3 = lhs3 - rhs3
        answer4 = lhs4 - rhs4
    if op == '*':
        answer1 = lhs1 * rhs1
        answer2 = lhs2 * rhs2
        answer3 = lhs3 * rhs3
        answer4 = lhs4 * rhs4

    return max(answer1, answer2, answer3, answer4)


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    no_of_nos = int((len(dataset) + 1) / 2)
    max_matrix = np.zeros((no_of_nos, no_of_nos), dtype=int)
    min_matrix = np.zeros((no_of_nos, no_of_nos), dtype=int)

    current_start_idx_for_dataset = len(dataset) - 1

    for i in range(no_of_nos - 1, -1, -1):
        for j in range(i, no_of_nos):
            # no_of_operations = j - i
            if i == j:
                max_matrix[i][j] = int(dataset[current_start_idx_for_dataset])
                min_matrix[i][j] = int(dataset[current_start_idx_for_dataset])
            else:
                current_operation_idx = current_start_idx_for_dataset + 1
                rhs_row_num = 1
                for k in range(i, j):
                    # Max and Max
                    lhs1 = max_matrix[i][k]
                    rhs1 = max_matrix[i + rhs_row_num][j]
                    # Max and Min
                    lhs2 = max_matrix[i][k]
                    rhs2 = min_matrix[i + rhs_row_num][j]
                    # Min and Max
                    lhs3 = min_matrix[i][k]
                    rhs3 = max_matrix[i + rhs_row_num][j]
                    # Min and Min
                    lhs4 = min_matrix[i][k]
                    rhs4 = min_matrix[i + rhs_row_num][j]
                    op = dataset[current_operation_idx]
                    result_min = compute_min(lhs1, rhs1, lhs2, rhs2, lhs3, rhs3, lhs4, rhs4, op)
                    result_max = compute_max(lhs1, rhs1, lhs2, rhs2, lhs3, rhs3, lhs4, rhs4, op)
                    if max_matrix[i][j] == 0 or result_max > max_matrix[i][j]:
                        max_matrix[i][j] = result_max
                    if min_matrix[i][j] == 0 or result_min < min_matrix[i][j]:
                        min_matrix[i][j] = result_min
                    current_operation_idx += 2
                    rhs_row_num += 1

        current_start_idx_for_dataset = current_start_idx_for_dataset - 2
    # print(max_matrix)
    # print(min_matrix)
    return max_matrix[0][no_of_nos - 1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
    # print(find_maximum_value("5-8+7*4-8+9"))
