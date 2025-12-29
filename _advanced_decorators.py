def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} to  {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0 # Add a counter attribute to the wrapper
    return wrapper

@call_counter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

'''
Output:
Call 1 to  greet
Hello, Alice!
Call 2 to  greet
Hello, Bob!
'''