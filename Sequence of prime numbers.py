import math

def prime_sequence(upper_limit):
    primes = [2]                      
    
    for i in xrange(3,upper_limit,2):
        x = math.sqrt(i)
        isprime = True
        for j in primes:               
            if j <= x:
                if i%j == 0:
                    isprime = False
                    break
    
        if isprime:
            primes.append(i)

    return primes
    
def set_prime(num):
    "num is a prime; set all of its multiples in is_prime to zero"
    for x in xrange(num*2, N, num):
        is_prime[x] = 0

def prime_sequence2(N):

    # initialize an array of flags
    is_prime = [1 for num in xrange(N)]
    is_prime[0] = 0 # this is because indexing starts at zero
    is_prime[1] = 0 # one is not a prime, but don't mark all of its multiples!


    # iterate over all integers up to N and update the is_prime array accordingly
    for num in xrange(N):
        if is_prime[num] == 1:
            set_prime(num)

    primes = [num for num in xrange(N) if is_prime[num]]
    
    print primes
