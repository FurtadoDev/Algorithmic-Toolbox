# python3

from random import randint

global_array = []


def partition3(array, left, right):
    # condition when left and right are very close
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < array[left]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i = i + 1
    temp = array[i-1]
    array[i-1] = array[left]
    array[left] = temp
    # return the index around which the array is partitioned
    return i-1


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    # make pivot first
    array[left], array[k] = array[k], array[left]
    # make a call to partition3 and then two recursive calls
    # to randomized_quick_sort
    partition_idx = partition3(array, left, right)
    randomized_quick_sort(array, left, partition_idx - 1)
    randomized_quick_sort(array, partition_idx + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
