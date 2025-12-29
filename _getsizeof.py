import sys

class MyClass:
    my_var = "foo"

my_list = [MyClass()] * 10000000
print(len(my_list)) # 10000000

print(sys.getsizeof(my_list)) # 80000056