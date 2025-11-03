import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(s):
    print(f"Sleeping for {s} seconds")
    time.sleep(s)
    return s

def poolingDemo():
    with ThreadPoolExecutor() as e:
        l = [3, 5, 1, 2]
        results = e.map(func, l)
        for result in results:
            print(result)

poolingDemo()