# #2.1
# def get_month_season(month):
#     month = raw_input("Enter the abbreviation for month: ")
#     if month == "jan" or month == "feb" or month == "dec":
#         return "Winter"
#     elif month == "mar" or month == "apr" or month == "may":
#         return "Spring"
#     elif month == "jun" or month == "jul" or month == "aug":
#         return "Summer"
#     elif month == "sep" or month == "oct" or month == "nov":
#         return "Fall"
# pass
#
#
#
# def month_info(month, category):
#
#     full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
#                   'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
#                   'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}
#
#     month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
#                   'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
#
#     birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
#                     'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
#                     'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}
#
#     category = raw_input("Enter the category: ")
#
#     if category == "full_names":
#         return full_names[month]
#
#     elif category == "month_nums":
#         return month_nums[month]
#
#     elif category == "birth_stones":
#         return birth_stones[month]
#
# print month_info(str,str)
# print get_month_season(str)
#
#
#
#
# #2.2
# def perfect_square(num):
#     if num in set(i**2 for i in range(num+1)):
#         return True
#     else:
#         return False
# pass
#
# def next_perfect_square(num):
#     num = int(raw_input("Enter a number: "))
#     if perfect_square(num):
#         return int((num**0.5+1)**2)
#     else:
#         return -1
#
# print next_perfect_square(int)

#2.3
import random

def flip_coin():
    x = random.random()
    if x > 0.5:
        return "H"
    else:
        return "T"
    pass

def roll_die():
    y = random.randint(1,6)
    return y

    pass


# def flip_coin_roll_die(n_times):
#     n_times = int(raw_input("Flip and roll n times: "))
#     outcomes = []
#     for i in range(n_times):
#         x = flip_coin()
#         y = roll_die()
#         outcomes.append((x,y))
#     return outcomes
#
# print flip_coin_roll_die(int)

#3.1

# def model_dice_rolls():
#     first_player = int(raw_input("First player's rolls: "))
#     second_player = int(raw_input("Second player's rolls: "))
#     first_outcomes = []
#     second_outcomes = []
#     for i in range(first_player):
#         first_outcomes.append(roll_die())
#     for i in range(second_player):
#         second_outcomes.append(roll_die())
#     player1 = sum(first_outcomes)
#     player2 = sum(second_outcomes)
#     if player1 == player2:
#         print "Tie!"
#     elif player1 > player2:
#         print "Player 1 Wins!"
#     else:
#         print "Player 2 Wins!"
#     print (player1, player2)
# model_dice_rolls()


#3.2


def calc_total_bill(subtotal, tax, tip):
    bill_with_tax = float(subtotal)*(1+float(tax))
    bill_with_tax_and_tip = bill_with_tax*(1+float(tip))
    return bill_with_tax
    return bill_with_tax_and_tip
subtotal = raw_input("Enter the subtotal: ")
tax = raw_input("Enter the tax rate: ")
tip = raw_input("Enter the tip rate: ")
bill_with_tax, bill_with_tax_and_tip = calc_total_bill(subtotal, tax, tip)
print bill_with_tax
print bill_with_tax_and_tip
