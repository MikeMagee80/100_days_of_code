

# Lambda functions

# items = [   # list of tuples
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# # def sort_item(item):
# #     return item[1]


# # items.sort(key=sort_item)
# # print(items)

# items.sort(key=lambda item:item[1])  # (key=lambda parameters:expression)
# print(items)


#---------------------------------------

# Map function

# items = [   # list of tuples
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# # prices = []   # define empty list
# # for item in items:
# #     prices.append(item[1])

# x = map(lambda item: item[1], items)

# # print(prices)

# print(x)   # output: <map object at 0x102843040>

# for item in x:
#     print(item)

# # output: 
# # <map object at 0x10447b040>
# # 10
# # 9
# # 12

# prices = list(map(lambda item: item[1], items))
# print(prices)



#---------------------------------

# Filter function

# items = [   # list of tuples
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# # x = filter(lambda item: item[1] >= 10, items)
# # print(x)  # output: <filter object at 0x102d2f040>

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)  # output: [('Product1', 10), ('Product3', 12)]

#---------------------------------

# List Comprehensions

# items = [   # list of tuples
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]


# # prices = list(map(lambda item: item[1], items))
# prices = [items[1] for item in items]  # produces same result as line 83


# # filtered = list(filter(lambda item: item[1] >= 10, items))
# filtered = [item for item in items if item[1] >= 10] 

# print(prices)
# print(filtered)


#-----------------------------

# Zip function

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # combine 2 lists into a single list of tuples

# print(zip(list1, list2))  # output: <zip object at 0x1002a2c00>
# print(list(zip(list1, list2)))  # output: [(1, 10), (2, 20), (3, 30)]

# print(list(zip("abc", list1, list2)))   # output: [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

#-------------------------------


# Stacks

# LIFO - Last In First Out

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)   # output: [1, 2, 3]
# last = browsing_session.pop()
# print(last) # output: 3
# print(browsing_session) # output [1, 2]

# print("redirect", browsing_session[-1]) # output: redirect 2

# if not browsing_session:  # if browsing_session is empty
#     print ("disable")


#--------------------------

# Queues 

# FIFO - First In First Out

# from collections import deque 
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)  # output: deque([2, 3])

# if not queue:
#     print("empty")


#------------------------------

# Tuples

# A read-only List

# point = (1, 2, 3)   # parentheses can be dispensed and Python will see point = 1, 2 as a type:tuple as long as comma trails an item

# print(point[0])
# print(point[0:2])

# x, y, z = point
# if 10 in point:
#     print("exist")

#-----------------

# Swapping Variables

# x = 10
# y = 11

# # z = x
# # x = y
# # y = z
# # print("x", x)      # output: x 11
# # print("y", y)      # output: y 10

# x, y = y, x   # has same effect as above


#-------------------

# Arrays

# take less memory and are faster than Lists

# from array import array

# numbers = array("i", [1, 2, 3])   # every object in an Array should be of the same type


#-------------------

# Sets

# A collection with no duplicates

# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}

# print(first | second)  # output: {1, 2, 3, 4, 5}
# print(first & second) # output: {1}
# print(first - second) # output: {2, 3, 4}
# print(first ^ second) # output: {2, 3, 4, 5}

# # Cannot access objects in sets with an index

# if 1 in first:
#     print("yes")

#----------------------

# Dictionaries

# A collection of key:value pairs

# point = {"x": 1, "y": 2}

# point = dict(x = 1, y=2)
# print(point["x"]) # output: 1
# print(point) # output: {'x': 1, 'y': 2}
# point["z"] = 20
# print(point) # ouput: {'x': 1, 'y': 2, 'z': 20}

# if "a" in point:
#     print(point["a"])

# del point["x"]
# print(point) # output: {'y': 2, 'z': 20}

# for key in point:
#     print(key, point[key])

#-------------------------------

# Dictionary comprehensions

# values = []
# for x in range(5):
#     values.append(x * 2)

# values = [x * 2 for x in range(5)] # identical operation to 3 lines of code above

# print(values)  # output: [0, 2, 4, 6, 8]

# values = {x: x *2 for x in range(5)}
# print(values) # output: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}



#---------------

# Generator Expressions

# for dealing with very large data set

# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)

# from sys import getsizeof

# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))  # output: gen: 104
# values = [x * 2 for x in range(100000)]
# print("list:", getsizeof(values)) # output: list: 800984


#--------------------

# Unpacking Operator

# numbers = [1, 2, 3]
# print(*numbers)  # output: 1 2 3 


# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]
# print(values) # output: [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']

# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined)  # output: {'x': 10, 'y': 2, 'z': 1}

#-------------------------

# Exercise

# from pprint import pprint

# sentence = "This is a common interview question"

# # Determine most frequent item in the string

# char_frequency = {}  # create empty dictionary to hold char:num pairs
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# print(char_frequency)
# # {'T': 1, 'h': 1, 'i': 5, 's': 3, ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 't': 2, 'e': 3, 'r': 1, 'v': 1, 'w': 1, 'q': 1, 'u': 1}

# pprint(char_frequency, width=1)

# # take out each key:value pair, convert it into a tuple, put it in a list

# print(sorted(char_frequency.items()))  # returns all key:value pairs as tuples
# # [(' ', 5), ('T', 1), ('a', 1), ('c', 1), ('e', 3), ('h', 1), ('i', 5), ('m', 2), ('n', 3), ('o', 3), ('q', 1), ('r', 1), ('s', 3), ('t', 2), ('u', 1), ('v', 1), ('w', 1)]    List of unsorted tuples

# print(sorted(char_frequency.items(), key=lambda kv:kv[1])) # takes a key:value and returns the key value of 1
# #[('T', 1), ('h', 1), ('a', 1), ('c', 1), ('r', 1), ('v', 1), ('w', 1), ('q', 1), ('u', 1), ('m', 2), ('t', 2), ('s', 3), ('o', 3), ('n', 3), ('e', 3), ('i', 5), (' ', 5)]

# print(sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True)) 
# # [('i', 5), (' ', 5), ('s', 3), ('o', 3), ('n', 3), ('e', 3), ('m', 2), ('t', 2), ('T', 1), ('h', 1), ('a', 1), ('c', 1), ('r', 1), ('v', 1), ('w', 1), ('q', 1), ('u', 1)]

# char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True)
# print(char_frequency_sorted[0])
# # ('i', 5)    