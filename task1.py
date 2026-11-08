coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}

    for coin in coins:
        count = amount // coin

        if count > 0:
            result[coin] = count
            amount %= coin

    return result


def find_min_coins(amount):
    dp = [float("inf")] * (amount + 1)
    last_coin = [0] * (amount + 1)

    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                if dp[current_amount - coin] + 1 < dp[current_amount]:
                    dp[current_amount] = dp[current_amount - coin] + 1
                    last_coin[current_amount] = coin

    result = {}

    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


amount = 113

print("greedy:", find_coins_greedy(amount))
print("dynamic programming:", find_min_coins(amount))