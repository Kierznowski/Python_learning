# LIST COMPREHENSION

nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []

for n in nums:
    my_list.append(n*n)

print(my_list)

my_list = []
my_list = [n*n for n in nums]
print(my_list)

# LAMBDA EXAMPLE

my_list = map(lambda n: n*n, nums)
print(next(my_list))

my_list = []
for n in nums:
    if n%2 == 0: 
        my_list.append(n)

print(my_list)

my_list = []
my_list = [n for n in nums if n%2 == 0]
print(my_list)

# FILTER EXAMPLE

my_list = []
my_list = filter(lambda n: n%2==0, nums)
print(my_list)

# NESTED LISTS

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))

print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


# DICT_COMPREHENSION

names = ["Bruce", "Clark", "Peter", "Logan"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine"]

for z in zip(names, heroes):
    print(z)

my_dict = {}

for name, hero in zip(names, heroes):
    my_dict[name] = hero

print(my_dict)

my_dict = {name:hero for name, hero in zip(names, heroes) if name != "Peter"}
print(my_dict)

# SET COMPREHENSION

nums = [1,1,2,3,1,4,5,4,6,7,7,7,8,4,5,9]

my_set = set()

for n in nums:
    my_set.add(n)

print(my_set)

my_set = {n for n in nums}

print(my_set)

# GENERATOR EXPRESSIONS

nums = [1,2,3,4,5,6,7,8,9,10]

def generator(nums):
    for n in nums:
        yield n*n

squared = generator(nums)

for n in squared:
    print(n)

my_gen = (n*n for n in nums)

for n in my_gen:
    print(n)

