"""def func(n):
    c=1
    while c<=n:
        print('before yield')
        yield c
        print("after yield")
        c=c+1

itera=func(5)
print('after getting generator object')
for i in itera:
    print('before printing number')
    print(i)
    print("after printing number")"""

#example without loop in generator  function
"""def func():
    print('hello')
    yield 1
    yield 2
    yield 3

itera=func()
print('after getting generator object')
for i in itera:
    print('before printing number')
    print(i)
    print("after printing number")"""