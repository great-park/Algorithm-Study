from audioop import reverse


def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin_count*coin
        details.append([coin, coin_count])

    return total_coin_count, details


coin_list = [1, 100, 50, 500]
print(min_coin_count(4720, coin_list))
