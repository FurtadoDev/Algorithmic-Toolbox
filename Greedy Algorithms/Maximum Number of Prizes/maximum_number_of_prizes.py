# python3
import math


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9

    summands = []
    k = math.floor((-1 + math.sqrt(1 + (8*n)))/2)
    for i in range(1, k+1):
        summands.append(i)
    sum_of_k_summands = (k * (k + 1))/2
    remaining_candies = n - sum_of_k_summands
    summands[k-1] = summands[k-1] + remaining_candies

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
