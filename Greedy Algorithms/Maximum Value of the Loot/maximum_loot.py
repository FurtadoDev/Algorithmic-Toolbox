# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    weights_prices = []
    num_items = len(weights)
    for idx in range(0, num_items):
        temp_tuple = (weights[idx], prices[idx])
        weights_prices.append(temp_tuple)

    weights_prices.sort(reverse=True, key=lambda x: round(x[1]/x[0], 4))
    # print(weights_prices)
    loot_value = 0
    current_capacity = capacity
    array_index = 0
    while current_capacity > 0 and array_index < num_items:
        if weights_prices[array_index][0] >= current_capacity:
            loot_value = round(loot_value + (current_capacity*(weights_prices[array_index][1]/weights_prices[array_index][0])), 4)
            current_capacity = 0
        else:
            loot_value = round(loot_value + (weights_prices[array_index][0]*(weights_prices[array_index][1]/weights_prices[array_index][0])), 4)
            current_capacity = current_capacity - weights_prices[array_index][0]
        array_index = array_index + 1

    return loot_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
