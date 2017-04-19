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

def find_divisors(n):
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    return divisors
print find_divisors(21)

#1.2 LCM
