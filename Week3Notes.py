# def get_evens():
#     evens = []
#     for i in range(10):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens

# def r56():
#     return 56
#
#
#
# def my_odd_list(begin, up_to=100): #defaults
#     odd = []
#     for i in range(begin, up_to):
#         if i % 2 == 1:
#             odd.append(i)
#     return odd
#
#
# print my_odd_list(-4, 15).count(1)

# def my_divisor_list(begin, up_to, divisor):
#     elements = []
#     for i in range(begin, up_to):
#         if i % divisor == 0:
#             elements.append(i)
#     return elements
# print my_divisor_list(-11, 9, 5)


# List comprehensions
#list_we_are_building = [transform(thing) for thing in iterable]
squares = [i ** 2 for i in range (10)]
print squares

#squares = []
#for i in range(10):
#   squares.append(i**2)
#print squares

def transformation(x):
    return ((x-2)**3)
cubes = [transformation(i) for i in range(10)]
print cubes


odds = [i for i in range(10) if i % 2 == 1]
print odds

cubes = {i:i**3 for i in range(1,6)}
print cubes

from random import randint
animals = ['dog', 'cat', 'fish', 'horse']
dict = {animal:randint(1,10) for animal in animals}
print dict
