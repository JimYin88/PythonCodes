def prime_factors(n):
    result = []
    remainder = n
    factor = 2
    while remainder > 1:
        if remainder % factor == 0:
            result.append(factor)
            remainder /= factor
        else:
            if factor == 2:
                factor = 3
            else:
                factor += 2
            
    return result
