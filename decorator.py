def decorator(func):
    def wrapper():
        print("hello")
        func()
        print("world")
        return 9
    return wrapper

@decorator
def greet():
    print("hello world")

r=greet()
print(r)