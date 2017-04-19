#WARM-UP 1

#user_input = raw_input('String to add to end of my_str: ')
#my_str = "This String wasn't Chosen Arbitrarily... "


#if len(user_input) < 10:
#    my_str += user_input

#print my_str


#WARM-UP 2

#my_list = [1, 'hello', 2, 'there', 3, 'list']
#user_input= raw_input("Enter something for my_list: ")
#if len(user_input) < 8:
#    my_list.append(user_input)
#else: my_list.append(4)
#print my_list


#WARM-UP 3

# user_number = int(raw_input('Min length to be printed: '))
# my_list = ['hello', 'there', 'python', list('list'), '!']
# longer_elements = []
# for element in my_list:
#     if len(element) >= user_number:
#         longer_elements.append(element)
# print longer_elements


my_list = ['hello', 'there', 'python', list('list'), '!']
for idx, element in enumerate(my_list):
    if idx % 2 == 0:
        print (element)
