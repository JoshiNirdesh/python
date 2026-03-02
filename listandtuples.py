# list = [1,54,21,23,2]
# print(list[1:3])
# list.append(12)

# # list.sort()
# # list.sort(reverse = True)
# list.reverse()
# print(list)
# list.remove(1)
# print(list)
# list.pop(2)
# print(list)

# tup = (1,2,56,22,21,78,2)

# print(tup)
# print(type(tup))

# print(tup.index(2))
# print(tup.count(2))

# movie = []

# mov1 = movie.append(input("Enter a first movie: "))
# mov2 = movie.append(input("Enter a second movie: "))
# mov3 = movie.append(input("Enter a third movie: "))

# print(movie)

list = [1,2,3,2,1]
orglist = list.copy()
list.reverse()

if orglist == list:
    print("Palindrome")
else:
    print("Not palindrome")
