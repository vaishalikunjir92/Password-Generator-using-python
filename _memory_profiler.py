from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(100000)] # Consumes memory
    b = [i*2 for i in a] # more memory consumption
    return b

if __name__ == "__main__":
    my_function()

''' Output 

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3     22.2 MiB     22.2 MiB           1   @profile
     4                                         def my_function():
     5     26.8 MiB      4.6 MiB      100003       a = [i for i in range(100000)] # Consumes memory
     6     30.6 MiB      3.8 MiB      100003       b = [i*2 for i in a] # more memory consumption
     7     30.6 MiB      0.0 MiB           1       return b
'''
