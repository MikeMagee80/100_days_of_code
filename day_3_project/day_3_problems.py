
# Exercise 1: Odd or Even
# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
# import random
# #Write the rest of your code below this line 👇

# # You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# # Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# # There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# # e.g. 1 means Heads 0 means Tails

# random_side = random.randint(0, 1)

# if random_side == 1:
#     print('Heads')
# else:
#     print('Tails')
# ================================

# Exercise 2: BMI 2.0

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# bmi = weight / (height**2)
# rounded_bmi = round(bmi)

# if bmi < 18.5:
#     print(f"Your BMI is {rounded_bmi}, you are underweight.")
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
# elif bmi > 25 and bmi < 30:
#     print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
# elif bmi > 30 and bmi < 35:
#     print(f"Your BMI is {rounded_bmi}, you are obese.")
# else:
#     print(f"Your BMI is {rounded_bmi}, you are clinically obese.")

# ==================

# Exercise 3: Leap Year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True  # Divisible by 400, so it's a leap year
#             else:
#                 return False  # Divisible by 100 but not 400, not a leap year
#         else:
#             return True  # Divisible by 4 but not 100, so it's a leap year
#     else:
#         return False  # Not divisible by 4, not a leap year

# # Prompt the user for input


# # Call the function and display the result
# if is_leap_year(year):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

# ==============================
