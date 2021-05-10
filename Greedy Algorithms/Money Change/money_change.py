# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    current = 0
    minimum_number_coins = 0
    while current < money:
        if (current + 10) <= money:
            current = current + 10
            minimum_number_coins = minimum_number_coins + 1
        elif (current + 5) <= money:
            current = current + 5
            minimum_number_coins = minimum_number_coins + 1
        else:
            current = current + 1
            minimum_number_coins = minimum_number_coins + 1

    return minimum_number_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
