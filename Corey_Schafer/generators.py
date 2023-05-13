#Classic aproach

"""
def squares(numbers):
    for i in numbers:
        squared.append(i*i)
    return squared

squared = []

numbers = [1, 2, 3, 4, 5]

print(squares(numbers))

"""
#Generator

def squares(numbers):
    for i in numbers:
        yield i*i

numbers = [1, 2, 3, 4, 5]

squared_nums = squares(numbers)

"""
print(next(squared_nums))
print(next(squared_nums))
print(next(squared_nums))
"""
"""
for num in squared_nums:
    print(num)
"""

print(list(squared_nums))

#Generator with list comprehension

my_nums = (i*i for i in numbers)
print(list(my_nums))

#Generators are faster and needs less memory than ordinary lists