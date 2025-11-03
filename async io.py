#executing on a single thread as per gil(global interpreter lock)
"""The Global Interpreter Lock (GIL) in Python is a mutex (mutual exclusion lock)
 that ensures only one thread can execute Python bytecode at any given time within a single Python process.
"""
import asyncio

async def func1():
    print("func1")
async def func2():
    print("func2")
async def func3():
    print("func3")

async def main():
    """await func1()
    await func2()
    await func3()"""
    await asyncio.gather(func1(),func2(),func3())

asyncio.run(main())