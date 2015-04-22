def coin_change(amount, coins):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif len(coins) == 0:    
        return 0
    else:
        return coin_change(amount - coins[0], coins) + coin_change(amount, coins[1:])


def memoized(func):
    cache={}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

coin_change = memoized(coin_change)

if __name__ == '__main__':
    
    N, M = list(map(int, raw_input().split()))
    coins = tuple(map(int, raw_input().split()))
    
    print coin_change(N, coins)
