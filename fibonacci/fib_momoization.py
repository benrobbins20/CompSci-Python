def sanitize_input():
    n = input('Enter Nth term: ')
    if n.isdigit():
        n = int(n)
        if n < 0 and not isinstance(n, int):
            print('Incorrect input')
    return n
            
fib_cache = {}    
def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n] # dictionary, so key will be the n value, and value will be the fibonacci(n)
    if n == 1:
        return n
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = value
    return value

from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci_cached(n):
    if n == 1:
        return n
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


    
for n in range(1,sanitize_input()):
    print(n, ':', fibonacci(n)) # uses manual cacheing 
    
for n in range(1,sanitize_input()):
    print(n, ':', fibonacci_cached(n)) # uses builin cacheing
    
    
    
    
    
    
    
    

    
    
    