
# LISTS

# letters = ["a", "b", "c"]

# matrix = [[0,1 ], [2, 3]] # a list of multiple lists is a matrix

# zeros = [0] * 5

# combined = zeros + letters # concatenates both lists into a single list

# numbers = list(range(20))  # creates a list of numbers from 0 to 19

# chars = list("Hello World")

# print(chars)

# print(len(chars))

#---------------------------

# Accessing items in a list

# letters = ["a", "b", "c", "d"]
# print(letters[0])
# print(letters[-1])
# print(letters[0:3])
# print(letters[::2])

# letters[0] = "A"
# print(letters)


# numbers = list(range(20))
# print(numbers)
# print(numbers[::2])  # returns every other element in list

# numbers = list(range(20))
# print(numbers[::-1])  # returns every element in list, in reverse order (counting down)


#-----------------------

# List Unpacking

# numbers = [1, 2, 3]

# first, second, third = numbers  # number of variables on the left side of the operator must equal those in the list

# numbers = [1, 2, 3, 4, 4, 4, 4, 4]
# first, second, *other = numbers

# print(first, second)
# print(other)



#---------------

# Looping Over Lists

# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)

# letters = ["a", "b", "c"]
# for letter in enumerate(letters):  # returns each iteration as a tuple of the index and the item at that index
#     print(letter)
#     print(letter[0], letter[1])


# letters = ["a", "b", "c"]
# items = (0, "a")
# index, letter = items
# for index, letter in enumerate(letters):
#     print(index, letter)

#--------------------------

# Looping over a list

# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)


# for letter in enumerate(letters):
#     print(letter)

# output:

# a
# b
# c
# (0, 'a')
# (1, 'b')
# (2, 'c')


# letters = ["a", "b", "c"]
# items = (0, "a")
# index, letter = items
# for letter in enumerate(letters):
#     print(letter[0], letter[1])

# output:

# 0 a
# 1 b
# 2 c

# letters = ["a", "b", "c"]

# for index, letter in enumerate(letters):
#     print(index, letter)
#---------------------

# Adding or removing items

# letters = ["a", "b", "c"]

# Add

# letters.append("d")  # adds item to end of list
# print(letters)

# Output:
# ['a', 'b', 'c', 'd']  

# letters.insert(0, "-") # adds item to the list at the desired index
# print(letters)

# Remove

# letters.pop()
# print(letters)

# Output:
# ['a', 'b']

# letters.pop(0)
# print(letters)

# Output:
# ['b', 'c']

# letters.remove("b") # will remove 1st occurence of letter "b"
# print(letters)

# del letters[0:3] # deletes a range of items in the list

# letters.clear # deletes all items in the list


#-----------------

# Finding items

# letters = ["a", "b", "c"]

# print(letters.index("a"))

# if "d" in letters:    # allows program to run without returning an error if item is not present in list
#     print(letters.index("d"))

# print(letters.count("b"))   # prints number of occurences of item in list

#----------------------

# Sorting lists

# numbers = [3, 51, 2, 8, 6]
# numbers.sort()   # sorts list in ascending order (modifying original list)
# print(numbers)

# output:
# [2, 3, 6, 8, 51]

# numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)  # sorts list in descending order
# print(numbers)

# numbers = [3, 51, 2, 8, 6]
# # numbers.sort()
# print(sorted(numbers))  # returns new list that is sorted
# # print(sorted(numbers, reverse=True)) 
# print(numbers)

# output:
# [2, 3, 6, 8, 51]
# [3, 51, 2, 8, 6]



# items = [   # list of tuples
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

# output:
# [('Product2', 9), ('Product1', 10), ('Product3', 12)]  (sorted by price)

#-------------------------------

