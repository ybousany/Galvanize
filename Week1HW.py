#FINDING THE LCM

#num1 = int(raw_input("Enter a number: "))

#num2 = int(raw_input("Enter a number: "))

#num3 = num1 * num2

#while num3 >= num1 and num3 >= num2:
#    if num3 % num1 == 0 and num3 % num2 == 0:
#        x = num3
#    num3 -= 1
#print (x)

# #DETERMINING PRIME NUMBERS
#
# num1 = int(raw_input("Enter a number: "))
# num2 = 2
# x = "prime"
# if num1 == 1:
#     x = "not prime"
# while num1 > num2:
#     if num1 % num2 == 0:
#         x = "not prime"
#     num2 +=1
# print (x)
#
#
# #SERIES a_0=1; a_(n+1)= 2a_n+1
#
# n = int(raw_input("Enter a number: "))
# a = 0
# for i in range (1,n+1):
#     y = 2*a+1
#     a = y
# print (y)





#Challenge Problem
for a in range (1,7):
    for b in range (1,7):
        for c in range (1,7):
            for d in range (1,7):
                for e in range (1,7):
                    for f in range (1,7):
                            if (a + (b - c) * d - e) * f == 75:
                                ans = (a, b, c, d, e, f)
                                if len(ans)==len(set(ans)):
                                #if a != b and a != c and a != d and a != e and a != f and b != c and b != d and b != e and b != f and c != d and c != e and c != f and d != e and d != f and e != f:
                                    print (ans)
