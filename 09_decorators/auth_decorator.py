from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role.lower() != "admin":
            print(f"Access denied: Admins only")
            return None
        else:
            return func(user_role)

    return wrapper


@require_admin
def access_tea_inventory(role):
    print(f"Access granted to tea inventory")


access_tea_inventory("Admin")
access_tea_inventory("User")


"""

Caching Expensive Calculations-------------->
You are optimizing performance for a system that frequently repeats the same heavy calculations (e.g., a backend system or a financial calculator).



Tasks:

- Create a decorator called cache_results:
Use a dictionary to store past results based on arguments.
If the same arguments are passed again, return the cached result.
Otherwise, compute the result, cache it, and return the new value.
- Apply it to a function multiply(a, b):
It simply returns the product of two integers.
- The decorated function should:
Return "Computed: result" for new computations.
Return "From Cache: result" for repeated calls with the same arguments.

"""

# This function will be tested automatically.
# Do not change the function name or parameters.

from functools import wraps


def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return f"From Cache: {cache[args]}"
        else:
            result = func(*args)
            cache[args] = result
            return f"Computed: {result}"

    return wrapper


@cache_results
def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print(multiply(3, 4))
    print(multiply(5, 6))
    print(multiply(3, 4))
    print(multiply(5, 6))
