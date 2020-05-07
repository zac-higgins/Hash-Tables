import math
import random
import time

factorial_cache = {}
floor_and_mod_cache = {}

# ----------original function ------------#
# def slowfun(x, y):
#     # TODO: Modify to produce the same results, but much faster
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v

# ----------optimized function ------------#

# possibly write a factorial function and cache it's results??

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    v = math.pow(x, y)
    if v not in factorial_cache:
        factorial_cache[v] = math.factorial(v)
        v = factorial_cache[v]
    elif v in factorial_cache:
        v = factorial_cache[v]
    v //= (x + y)
    v %= 982451653

#     return v

# def slowfun(x, y):
#     # TODO: Modify to produce the same results, but much faster
#     v = math.pow(x, y)
#     # v = math.factorial(v)
#     if v not in factorial_cache:
#         factorial_cache[v] = math.factorial(v)
#         v = factorial_cache[v]
#     elif v in factorial_cache:
#         v = factorial_cache[v]
#     if v not in floor_and_mod_cache:
#         v //= (x + y)
#         v %= 982451653

#     return v

# Do not modify below this line!

start_time = time.time()
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
end_time = time.time()

print(f"Time: {end_time - start_time} seconds")