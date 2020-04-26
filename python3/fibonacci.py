# memoize creates a local cache for previously computed values
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be of type int")
    if n < 1:
        raise ValueError("n must be a positive int")
    if n in (1, 2):
        return 1
    elif n > 2:
        return fibonacci(n-2) + fibonacci(n-1)

for n in range(1,11):
    print(n, ":", fibonacci(n))
