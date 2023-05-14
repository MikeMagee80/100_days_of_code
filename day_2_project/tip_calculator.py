# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

total_bill = input("What was the total bill? ")

tip = input("What percentage tip would you like to give? ")

number_people = input("How many people to split the bill? ")

percent_tip = int(tip) * 0.01
total_money = float(total_bill) * (1 + percent_tip)
divided_money = total_money / int(number_people)

# rounded_split = round(divided_money, 2)
rounded_split = "{:.2f}".format(divided_money)

print(percent_tip)
print(total_money)
print(divided_money)
print(rounded_split)
