from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print(f"Hello from decorator lecture")


greet()
print(greet.__name__)
