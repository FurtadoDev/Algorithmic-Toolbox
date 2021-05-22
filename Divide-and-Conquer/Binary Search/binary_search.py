# python3
import math

data_set = []


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def recurse(l_idx, r_idx, check_for):
    global data_set
    if l_idx == r_idx:
        if data_set[l_idx] == check_for:
            return l_idx
        else:
            return -1
    else:
        mid_idx = math.floor((l_idx + r_idx)/2)
        if check_for <= data_set[mid_idx]:
            return recurse(l_idx, mid_idx, check_for)
        else:
            return recurse(mid_idx+1, r_idx, check_for)


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    global data_set
    data_set = keys
    data_set_size = len(keys)
    index = recurse(0, data_set_size-1, query)
    return index


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
