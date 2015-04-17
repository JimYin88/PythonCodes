def coin_change(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for c in coin_change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in coin_change(n, coins_available[1:], coins_so_far):
            yield c
            
n = 15
coins = [1, 5, 10, 25]
solutions = [s for s in coin_change(n, coins, [])]
for i in solutions:
    print i
    
print 'Optimal solution is', min(solutions, key=len)
