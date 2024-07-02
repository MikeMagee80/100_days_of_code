

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

# items.sort(key=lambda item:item[1])  # (key=lambda paramteres:expression)
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

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# # combine 2 lists into a single list of tuples

# print(zip(list1, list2))  # output: <zip object at 0x1002a2c00>
# print(list(zip(list1, list2)))  # output: [(1, 10), (2, 20), (3, 30)]

# print(list(zip("abc", list1, list2)))   # output: [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

#-------------------------------


# Stacks
