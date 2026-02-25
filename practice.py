# print("Hello, Nirdesh Welcome to python")

# name = "Nirdesh"
# age = 23 
# height = 5.8

# print("Hello I am "+ name + "Age",age, "height",height)

# name = input("Enter your name")
# age = int(input("Enter a age"))

# print("Hello, "+name+" you will be",age+1,"next year")

# number = int(input("Enter a number "))

# if number%2==0:
#     print(number,"is even number")
# else:
#     print(number,"is odd number")


# marks = int(input("Enter a marks"))

# if marks >90 :
#     print("A+")
# elif marks>80 and marks<=90:
#     print("B")
# elif marks>70 and marks <=79:
#     print("C")
# else :
#     print("Fail")


# nums = range (1,11)
# for num in nums:
#     print(num)

# i = 1 

# while i<=10:
#     print(i)
#     i+=1

# for num in range(1,11):
#     print("5 *",num,"=",num*5)

# numbers = [1,2,3,4,5]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

numbers = []

for i in range(5):
    num = int(input(f"Enter {i}  number"))
    numbers.append(num)

for even in numbers:
    if even%2==0:
        print(even)    