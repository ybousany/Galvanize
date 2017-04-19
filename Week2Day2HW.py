#WARM-UP 1:

# my_tup = ('diamond', 'club', 'spade', 'heart')
# print my_tup[::2]

#WARM-UP 2:
# my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'New York City'}
# my_dict = {'Massachusetts':'Boston', 'Colorado': 'Denver'}
# my_dct=dict(my_dct.items()+my_dict.items())
# user_input=raw_input("Type a state name: ")
# if user_input in my_dct:
#     print my_dct[user_input]
# else:
#     print "Capital not found"

# #WARM-UP 3:
# my_set = {2, 3, 5}
# my_fave_primes = {2, 11, 13, 23}
# my_intersect = my_set.intersection(my_fave_primes)
# for i in my_set.union(my_fave_primes):
#     if i in my_intersect == False:
#         print i

#2.2
# my_dct = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
# 'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
# 'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
# user_input=raw_input("Type a state name: ")
# if user_input.capitalize() in my_dct:
#    print my_dct[user_input.capitalize()]
# else:
#    print "Capital unknown"

#1.1
# user_input=raw_input("Input numbers: ")
# nums = user_input.split(',')
# tuple_list = []
# for i in zip(nums[::2], nums[1::2]):
#     tuple_list.append(i)
# print tuple_list

#2.1
# user_input = raw_input("Input numbers: ")
# names = user_input.split('-')
# my_dict = {}
# for i in names:
#     x = int(i)
#     my_dict[x]=x**2
# print my_dict

#3.1
# user_input1= raw_input("Input numbers 1: ")
# user_input2= raw_input("Input numbers 2: ")
# names1 = user_input1.split('-')
# names2 = user_input2.split('-')
# my_set1 = {i for i in names1}
# my_set2 = {i for i in names2}
# my_intersection = my_set1.intersection(my_set2)
# print ','.join(my_intersection)

#3.2
#
# user_input= raw_input("Enter words: ")
# my_set = {i for i in user_input.split(', ')}
# print ', '.join(my_set)

#3.3

# my_set=set()
# i=1
# while i==1:
#     user_input=raw_input("Enter a word: ")
#     if user_input=='v':
#         print ', '.join(my_set)
#     if user_input=='q':
#         break
#     else:
#         my_set.update(user_input.split())


#2.3
my_dict={}
while True:
    entry=raw_input("Enter a number, word: ")
    if not entry:
        break
    x, y, word = entry.split(',')
    my_dict[(x,y)] = word
while True:
    lookup = raw_input("Look up a coordinate: ")
    if lookup == 'q':
        break
    coord = tuple(lookup.split(','))
    if coord not in my_dict:
        print 'Coordinate not found'
    else:
        print my_dict[coord]
