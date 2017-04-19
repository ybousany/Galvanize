# FINDING THE GCF

# num1 = int(raw_input("Enter a number: "))
#
# num2 = int(raw_input("Enter a number: "))
#
# num3 = 1
# while num3 <= num1 and num3 <= num2:
#     if num1 % num3 == 0 and num2 % num3 == 0:
#         x = num3
#     num3 += 1
# print(x)

# # FACTORIAL
# user_input = int(raw_input('Please input a number to compute the factorial of: '))
#
# factorial = 1
#
# for i in range (1, user_input):
#     factorial *= user_input
#     user_input -= 1
#
# print factorial

#PRIME
num1 = int(raw_input("Enter a number: "))
num2 = 2
x = "prime"
if num1 == 1:
    x = "not prime"
for i in range (2, num1):
    if num1 % num2 == 0:
        x = "not prime"
    num2 +=1
print (x)
