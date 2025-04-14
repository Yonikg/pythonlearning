def my_beautiful_func():
    print('I am a such beautiful function.')

def do_something(activity):
    return f'I am {activity}'
def make_square(n):
    return n * n

def add_two_nums(a, b):
    return a + b

def create_list_of_nums():
    names = []
    while True:
        name = input('Enter names ? ')
        if name == 'quit':
            break
        names.append(name)
    return names

def filter_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens