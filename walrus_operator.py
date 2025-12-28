# code to check key exists in dictionary or not

my_dict = {'one':1, 'two':2, 'three':3, 'four':4}
def my_func(my_dict):
    if my_var := my_dict.get('my_var', None):
        return my_var

my_func(my_dict)