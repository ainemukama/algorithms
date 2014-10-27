from collections import defaultdict

def min_coin_sum(S, coin_values):
    mincoins = defaultdict(int)
    for val in range(1, S+1):
        mincoins[val] = min(1 + mincoins[val-coin] for coin in coin_values if val >= coin)
    return mincoins[S]

coin_values = [1, 5, 10, 21, 25]
print min_coin_sum(1, coin_values)
print min_coin_sum(5, coin_values)
print min_coin_sum(10, coin_values)
print min_coin_sum(25, coin_values)
print min_coin_sum(44, coin_values)
