""" Decorator Samples """
from functools import wraps

""" Simple Decorator: does not decorate functions with arguments """
def uppercase(func):

    @wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

def underline(func):

    @wraps(func)
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

def emphasis(func):

    @wraps(func)
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

# Those wraps decorators, are responsible for transmit function metadata to wrapped ones
# Metadata Like docstrings and name

""" Argument Decorator: Handle Args and Kwargs to wrapped functions """

def trace(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'LOG: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'LOG: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper

"""
Multiple simple decorators usage.
Note that the activation order is bottom to top.
"""
@emphasis
@underline
@uppercase
def hello_world():
    return f"Hello World!"

@trace
def hello_date(day, month, year):
    return f"Hello, it's {day} of {month} from {year}!"


if __name__ == "__main__":
    print(hello_world())
    print(hello_date('friday', 'may', 2019))
