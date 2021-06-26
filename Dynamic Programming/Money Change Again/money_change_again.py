# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [1, 3, 4]
    dp_array = [0] * (money + 1)
    for i in range(1, money + 1):
        temp_min = float("inf")
        for j in range(0, len(coins)):
            if (i - coins[j]) >= 0:
                if(dp_array[i-coins[j]] + 1) < temp_min:
                    temp_min = dp_array[i-coins[j]] + 1
        dp_array[i] = temp_min
    return int(dp_array[money])


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
