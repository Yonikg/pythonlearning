
def func():
    def return_f (a,b,c):
        return a+b+c
    return return_f
print (func()(10,10,10))


def function(review):
    return review(1,2,3)
def func_review (a,b,c):
        return a+b+c
print (function(func_review))


nums = [1, 2, 3, 4, 5]

print(list(map(lambda n: n ** 3, nums)))



print(list(filter(lambda n: n % 2 == 0, nums)))