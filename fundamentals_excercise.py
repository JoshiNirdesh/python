# first = int(input("Enter a first number"))
# second = int(input("Enter a second number"))

# print("Sum",first+second)
# print("Product",first*second)
# print("Differnce",first-second)

# a = 20
# b = 30 

# a=a+b
# b=a-b
# a=a-b
# print("A",a,"B",b)

# num = int(input("Enter a number "))

# if num%2==0:
#     print(num,"is even number")
# else:
#     print(num,"is odd number")

# if num%5==0 and num%11==0:
#     print(num,"is divisible by 5 and 11")
# else:
#     print("Not divsible by 5 and 11")

# if num==0:
#     print("zero")
# elif num>0:
#     print(num ,"is a positive number")
# else:
#     print(num,"is a negative number")

# first = int(input("Enter a first number "))
# second = int(input("Enter a second number "))
# op = input("Enter a operator (+,-,/,*)")

# if op =="+":
#     print(first,"+ ",second," = ", first+second)
# elif op =="-":
#         print(first,"- ",second," = ", first-second)
# elif op=="*":
#         print(first,"x",second," = ", first*second)
# elif op=="/":
#         print(first,"/",second," = ", first/second)


# for num in range(1,50):
#     if(num%2==0):
#         print(num)  

# num = int(input("Enter a number "))

# for nums in range(1,11):
#     print(num," x ",nums," = ",num*nums)
# fac = 1
# for nums in range(1,num+1):
#     fac *=nums
# print("Factorials ", fac)

# text = input("Enter a string ")
# print(text.upper())
# print(text[::-1])

# vowels = "aeiouAEIOU"
# count=0
# for char in text:
#     if char in vowels:
#         count+=1

# print("Total vowels ", count)
# rev = text[::-1]
# if(text ==rev):
#     print("Given string is palindrome")
# else:
#     print("given string is not plaindrom")

# sen = input("Enter a sentence ")
# count = 0
# for word in sen:
#     if word == " ":
#         count +=1

# print("Space ", count)

# list = [1,45,23,12,2]
# # print(max(list))
# # print(min(list))
# # print(sum(list))

# for num in list:
#     if num%2==0:
#         print(num)
# print(list.sort(reverse=True))
# print(list)
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

string = input("Enter a string ")

rev = string[::-1]

if(string == rev):
    print("Palindrome")
else:
    print("Not palindrome")