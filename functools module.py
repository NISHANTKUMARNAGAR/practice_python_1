from functools import lru_cache
import time

@lru_cache(maxsize=None)
def func(n):
    time.sleep(2)
    return n*n

l=[1,2,3,4,3,2,1,9]
for i in l:
    print(func(i))