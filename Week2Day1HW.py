user_input = raw_input('String to add to end of my_str: ')
my_str = "This String wasn't Chosen Arbitrarily... "


if len(user_input) < 10:
    my_str += user_input

print my_str
