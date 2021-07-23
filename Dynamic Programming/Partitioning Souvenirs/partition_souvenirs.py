# python3

from itertools import product
from sys import stdin
import numpy as np


def dfs(k, nums, explored, current_sum, target_sum, start_index):
    if k == 0:
        return 1

    if current_sum > target_sum:
        return 0
    elif current_sum == target_sum:
        return dfs(k-1, nums, explored, 0, target_sum, 0)
    else:
        for i in range(start_index, len(explored)):
            if explored[i] == 0:
                explored[i] = 1
                if dfs(k, nums, explored, current_sum + nums[i], target_sum, i) == 0:
                    explored[i] = 0
                else:
                    return 1
        return 0


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    # No of partitions = 3 in this question
    k = 3
    input_size = len(values)
    explored = [0] * input_size
    list_sum = sum(values)
    if list_sum % k != 0:
        return 0
    else:
        return dfs(k, values, explored, 0, int(list_sum/3), 0)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
    # test_values = (1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25)
    # print(partition3(test_values))

