from functools import wraps


def memoize(function: callable) -> callable:

    cache = {}

    @wraps(function)
    def decorator(*args: any, **kwargs: any) -> dict[str]:
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]

    return decorator
