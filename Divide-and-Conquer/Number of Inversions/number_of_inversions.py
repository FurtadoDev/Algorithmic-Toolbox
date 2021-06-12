# python3
import math
from itertools import combinations

dataset = []
inversion_count = 0


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    global dataset
    global inversion_count
    dataset = a
    inversion_count = 0
    length_dataset = len(dataset)
    split(0, length_dataset - 1)

    answer = inversion_count
    inversion_count = 0
    return answer


def split(left_idx, right_idx):
    if left_idx == right_idx:
        return
    mid_idx = math.floor((left_idx + right_idx)/2)
    split(left_idx, mid_idx)
    split(mid_idx + 1, right_idx)
    count_inversions_using_merge(left_idx, mid_idx, mid_idx + 1, right_idx)
    return


def count_inversions_using_merge(left_low, left_high, right_low, right_high):
    global dataset
    global inversion_count

    temp_list = []  # [(right_high - left_low) + 1]
    temp_list_idx = 0
    i = left_low
    j = right_low
    while i <= left_high and j <= right_high:
        if dataset[i] < dataset[j]:
            temp_list.append(dataset[i])
            i += 1
        elif dataset[j] < dataset[i]:
            temp_list.append(dataset[j])
            j += 1
            inversion_count += (left_high - i) + 1
        else:
            temp_list.append(dataset[i])
            i += 1

    # the left side is incomplete and the right side is complete
    if i <= left_high and j > right_high:
        while i <= left_high:
            temp_list.append(dataset[i])
            i += 1

    # the left side is complete and the right side is incomplete
    if i > left_high and j <= right_high:
        while j <= right_high:
            temp_list.append(dataset[j])
            j += 1

    temp_list_idx = 0
    for idx in range(left_low, right_high + 1):
        dataset[idx] = temp_list[temp_list_idx]
        temp_list_idx += 1

    return


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
    # Beginning of test cases
    # print(compute_inversions([1, 2, 3]))
    # print(compute_inversions_naive([1, 2, 3]))
    # print(compute_inversions([3, 2, 1]))
    # print(compute_inversions_naive([3, 2, 1]))
    # print(compute_inversions([2, 3, 9, 2, 9]))
    # print(compute_inversions_naive([2, 3, 9, 2, 9]))
    # print(compute_inversions([1, 20, 6, 4, 5]))
    # print(compute_inversions_naive([1, 20, 6, 4, 5]))
    # print(compute_inversions([3, 2, 5, 9, 4]))
    # print(compute_inversions_naive([3, 2, 5, 9, 4]))
