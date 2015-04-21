from functools import wraps

def memo(func):
    cache = {}                             # Stored subproblem solutions
    @wraps(func)                           # Make wrap look like func
    def wrap(*args):                       # The memoized wrapper
        if args not in cache:              # Not already computed?
            cache[args] = func(*args)      # Compute & cache the solution
        return cache[args]                 # Return the cached solution
    return wrap         
    
    
def fib(i):
    if i < 2:
        return 1
    else:
        return fib(i-1) + fib(i-2)
        
fib = memo(fib)

fib(100)

def C(n,k):
    if k == 0: 
        return 1
    elif n == 0: 
        return 0
    else:
        return C(n-1,k-1) + C(n-1,k)
        
C = memo(C)

C(100, 50)
