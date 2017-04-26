# #WARM-UP 1
# def calc_beers_on_the_wall(n=99):
#     return 'There are {} bottles of beer on the wall'.format(n)
# print calc_beers_on_the_wall(88)
#
#
# #WARM-UP 2
# def check_elsa_fan(fan=True):
#     if fan == True:
#         return "I love Elsa!"
#     else:
#         return "Let It Go!"
# print check_elsa_fan(False)
#
# #WARM-UP 3
#
# def hello_name(name='Josh'):
#     return 'Hello {}'.format(name)
# print hello_name('Yonit')
#
# #WARM-UP 4
#
# def divisors(n, potential_divisor=3):
#     return n % potential_divisor == 0
# print divisors(n=40, potential_divisor=6)

#1.1 DIVISORS

# def find_divisors(n):
#     divisors = []
#     for i in range(1,n):
#         if n % i == 0:
#             divisors.append(i)
#     return divisors
# print find_divisors(21)

#1.2 LCM
# def find_lcm(m,n):
#     i=m*n
#     while i>=m and i>=n:
#         if i % m == 0 and i % n == 0:
#             x = i
#         i-=1
#     return x
# print find_lcm(14,8)

# #2.1
# def beers(n):
#     if n == 0:
#         return 'No beers left!'
#     else:
#         return '{} beers left'.format(n)
# print beers(0)
#
# #2.2
# def fans(name):
#     names_set=set({'Cary', 'Sean', 'Josh'})
#     if name in names_set:
#         return True
#     else:
#         return False
# print fans('Cary')

# #2.3
# def num_sum(n):
#     user_input = raw_input("Enter a list: ")
#     num_list = user_input.split(',')
#     x = 0
#     for i in num_list:
#         x += int(i)
#     return x
# print num_sum([])
#
# #2.4
# def num_product(n):
#     user_input = raw_input("Enter a list: ")
#     num_list = user_input.split(',')
#     x = 1
#     for i in num_list:
#         x *= int(i)
#     return x
# print num_product([])
#
# #2.5
# def check_evens(n):
#     user_input = raw_input("Enter a list: ")
#     num_list = user_input.split(',')
#     evens_list = []
#     for i in num_list:
#         if int(i) % 2 == 0:
#             evens_list.append(int(i))
#     return evens_list
# print check_evens([])

#FACTORIAL
def factorial(n):
    x = 1
    for i in range (1,n+1):
        x *=i
    return x
print factorial(5)

#PRIMES
def prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    else:
        return True
print prime(2)
