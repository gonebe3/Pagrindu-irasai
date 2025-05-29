#Debug

# numbers = [1, 2, 3, 4, 5, 6]
# for i in range(len(numbers)):
#     if (i) % 2 != 0:
#         print(numbers[i])

# Buggy Code: Print even numbers from a list.
# numbers = [1, 2, 3, 4, 5, 6]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])

# Intention: Practice summing numbers in a list using a for loop
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:   # 1
#     total = total + num
# print("Sum is:", total)  # 2

# Intention: Practice using conditionals to check even or odd numbers
# nums = [1, 2, 3, 4, 5]
# for i in nums:
#     if i % 2 == 0:      # 1
#         print(f"{i} is even")
#     else:               # 2
#         print(f"{i} is odd")

# Intention: Practice building a list of squares with a for loop
# squares = []
# for i in range(1, 6):   # 1
#     squares.append(i * i)  # 2
# print("Squares:", squares)  # 3

# Intention: finding the maximum element in a list using loops
# numbers = [3, 7, 2, 9, 5]
# max_num = numbers[0]
# for n in numbers:
#     if n > max_num:
#         max_num = n
# print("Max number is", max_num)

# # Intention: Practice using loops to calculate factorial of a number
# n = 5
# result = 0
# for i in range(1, n + 1):
#     result = i*i
# print(f"Factorial of {n} is {result}")

# Intention: Practice checking if a string is a palindrome
# s = "racecar"
# if s == s[::-1]:
#     print("is a palindrome")
# else:
#     print("not a palindrome")

# Intention: Practice summing even numbers in a range
# total = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         total += i
# print("Sum of even numbers:", total)


# Intention: Practice counting vowels in a string
# text = "Hello World"
# count = 0
# for ch in text:
#     if ch.lower() in ["a", "e", "i", "o", "u"]:
#         count += 1
# print("Vowel count:", count)

# Intention: Practice tuple unpacking order
# t = (10, 20)
# first,second = t
# print("First:", first, "Second:", second)

# Intention: Reverse a list using a loop

# items = [1, 2, 3, 4, 5]

# reversed_items = []

# for i in items[::-1]:

#     reversed_items.append(i)

# print("Reversed:", reversed_items)
 
# Intention: Sum all values in a dictionary
# data = {"a": 1, "bb": 2, "ccc": 3}
# sum_values = 0
# for key in data:
#     sum_values += data[key] #vietoje len reikejo saraso pavadinima paimti ir naudoti laužtiniu skliaustusm nes norime ne saraso ilgi pliusoti tarpusavyje, o values is zodyno
# print("Total:", sum_values)



# data = {"a": 1, "bb": 2, "ccc": 3}
# sum_values = 0
# for key in data:
#     sum_values += len(key)
# print("Total:", sum_values)





# TEORIJA



# suma = True + True + True + False # True = 1, False = 0
# print(suma)
 
# if type(1.0) == int:
#     print("True yra int tipo")

# import datetime
 
# # siandien_tik_data = datetime.date.today()
# # print(siandien_tik_data)
 
# siandien_laikas_ir_data = datetime.date.today()
# print(siandien_laikas_ir_data)
 
# gimimo_data = datetime.date(1990, 1, 1) # nauja data
# print(gimimo_data)
 
# print(siandien_laikas_ir_data - gimimo_data) # atimame dvi datas
# print(gimimo_data.year)
 














