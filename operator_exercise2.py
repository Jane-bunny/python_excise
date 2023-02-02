# Basic Operators

#Arithmetic Operators
number1 = 4 + 5 * 9 / 2.0
print(number1)

remainder = 22 % 2
print(remainder)

squared = 5 ** 2
cubed = 7 ** 3
print(squared)
print(cubed)

# Operators on string
nicetomeetyou = "nice" + " " + "to" + " " + "meet" + " " + "you"
print(nicetomeetyou)

lotsofloves = "love" * 10
print(lotsofloves)

# Operators with lists
big_number = [7, 8, 9, 10]
small_number = [1, 2, 3, 4]
all_numbers = big_number + small_number
print(all_numbers)

print(big_number * 3)

# Exercise
x = object()
y = object()

x_list = ["banana"] * 10
y_list = ["apple"] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing code
if x_list.count("banana") == 10 and y_list.count("apple") == 10:
    print("Almost there...")
if big_list.count('banana') == 10 and big_list.count('apple') == 10:
    print("Great!")