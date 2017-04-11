# FINDING THE GCF

num1 = int(raw_input("Enter a number: "))

num2 = int(raw_input("Enter a number: "))

num3 = 1
while num3 <= num1 and num3 <= num2:
    if num1 % num3 == 0 and num2 % num3 == 0:
        x = num3
    num3 += 1
print(x)
