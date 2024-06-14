# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
# import random	 
# #Write the rest of your code below this line 👇

# # You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# # Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# # There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# # e.g. 1 means Heads 0 means Tails

# import random

# random_side = random.randint(0, 1)

# if random_side == 1:
#     print('Heads')
# else:
#     print('Tails')


# random_side = random.randint(0, 1)
# if random_side == 1:
#     print('Heads')
# else:
#     print('Tails')


# ########################################


# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# 🚨 Remember to remove the print statement above when you submit.

# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# import random

# # Get the total number of items in the list.
# num_items = len(names)
# # Generate random numbers between 0 and last index.
# random_choice = random.randint(0, num_items - 1)
# #Choose and print random name.
# print(f"{names[random_choice]} is going to buy the meal today!")


############################
