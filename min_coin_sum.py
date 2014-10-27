def coins(S, coin_values):
    min_coins = {0: 0}
    for val in range(1, S+1):
        min_coins[val] = min(1+min_coins[val-coin] for coin in coin_values if val >= coin)
    return min_coins[S]

coin_values = [1, 5, 10, 16, 25]
print coins(48, coin_values)
