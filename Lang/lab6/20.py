def cached(func):
    ch = {}
    
    def wrapper(*args, **kwargs):
        nonlocal ch
        print(ch)
        if not ch.get(args):
            g = func(*args, **kwargs)
            ch[args] = g
            return g
        else:
            return ch[args]

    return wrapper

@cached
def fib(n): 
    if n == 1 or n == 2: 
        return 1 
    else: 
        return fib(n - 1) + fib(n - 2)

print(fib(6))