# for number in range(3):
#     print("Attempt")
#     print("Attempt", number) 

# Attempt              output is such because the loop architecture is sequential within the loop.
# Attempt 0
# Attempt
# Attempt 1
# Attempt
# Attempt 2

#####################

# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * '.')  

# Output:
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...


#####################

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

# Output:
# Attempt 1 .
# Attempt 3 ...
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........


###############################

# booga = [1, 2, 3, 4]

# for x in booga:
#     print(x)


###############################

# Exercise 1: Print First 10 natural numbers using for loop

# for num in range(1, 11):
#     print(num)

##############################

# # Exercise 2: Print the following pattern
# # Write a program to print the following number pattern using a loop.

# print("Number Pattern ")

# # Decide the row count. (above pattern contains 5 rows)
# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times

# for i in range(1, row + 1, 1):    #range begins at 1, goes up to (but not inclusive of) row + 1 (6), in increments of 1
#     # Run inner loop i+1 times
#     for j in range(1, i + 1): #inner loop runs from 1 to i + 1 (so initial return is 1, since i + 1 = 2, and the range doesn't include 2 at this time)
#         print(j, end='@') # end= causes the j value to print without a newline, for the current iteration of the loop
#     #empty line after each row
#     print("")

# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

####################################

