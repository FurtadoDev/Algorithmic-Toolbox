# python3
from collections import namedtuple


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    # Base cases
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 3]
    dp_array = [0] * (n + 1)
    prev_elements = [0] * (n + 1)
    for i in range(2, n + 1):
        temp_min = float("inf")
        temp_prev_element = 0

        if i % 2 == 0:
            if (dp_array[int(i / 2)] + 1) < temp_min:
                temp_min = dp_array[int(i / 2)] + 1
                temp_prev_element = int(i / 2)
        if i % 3 == 0:
            if (dp_array[int(i / 3)] + 1) < temp_min:
                temp_min = dp_array[int(i / 3)] + 1
                temp_prev_element = int(i / 3)
        if (dp_array[i - 1] + 1) < temp_min:
            temp_min = dp_array[i - 1] + 1
            temp_prev_element = int(i - 1)

        dp_array[i] = temp_min
        prev_elements[i] = temp_prev_element

    # Backtrack to find the solution
    intermediate_numbers = [n]
    idx = n
    prev_element = prev_elements[idx]
    while prev_element != 1:
        prev_element = prev_elements[idx]
        intermediate_numbers.append(prev_element)
        idx = prev_elements[idx]

    intermediate_numbers.reverse()
    return intermediate_numbers


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
