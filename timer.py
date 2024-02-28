'''
A timer decorator used for printing the execution time of a class method

e.g. 
class Hello:
    @timer
    def func(self, *args, **kwargs):
        print('Hello World')
    
h = Hello()
h.func(1)

// Output: 
1 Hello World
2 Elapsed time of func(1): 0.0000000001s
'''
import time


def timer(func):
    def wrapper(*args, **kwargs):
        # Use the Time module the record the execution time of the method 
        start_time = time.perf_counter()

        # Store the return value of the method in the variable res
        res = func(*args, **kwargs)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        # Format the arguments and keyword arguments of the methods and print them out along with the runtime
        args = map(str, args[1:]) if args[1:] else ''
        kwargs = [f'{key}={kwargs[key]}' for key in kwargs] if kwargs else ''
        conn = ', ' if kwargs else ''
        print(f"Elapsed time of {func.__name__}({', '.join(args)}{conn}{', '.join(kwargs)}): {total_time:.10f}s")

        # Return the original return value of the method
        return res
    return wrapper


# Testing 
if __name__ == '__main__':
    class Hello:
        @timer
        def func(self, *args, **kwargs):
            print('Hello World')
        
    h = Hello()
    h.func(1, 't', end=0)
