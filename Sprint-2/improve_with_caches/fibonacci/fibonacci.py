# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    cache = {}

    def helper(i):
        if i <= 1:
            return i
        if i in cache:
            return cache[i]

        cache[i] = helper(i-1) + helper(i-2)
        return cache[i]

    return helper(n)