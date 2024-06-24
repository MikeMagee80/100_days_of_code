# def greet():
#     print("Hi there")
#     print("Welcome aboard")


# greet()

#------------------------------

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Mike", "Magee")
# print(" ")
# greet("John", "Smith")

#--------------------------------

# def greet(name):
#     print(f"Hi {name}")

# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting("Mike")
# print(message)

# file = open("content.txt", "w")  #creates .txt file content.txt, and opens it for writing
# file.write(message)


#--------------------------------

# def increment(number, by):
#     return number + by


# print(increment(number=2, by=1))  #keyword arguments to make code clearer


#--------------------------------

# def increment(number, by=1): #by is a default value
#     return number + by


# print(increment(2))  # by is a default, so unnecessary as argument in the call
# print(increment(2, 5)) # providing argument overrides the default

#-------------------------------

# def multiply(x, y):
#     return x * y

#VARIABLE NUMBER OF ARGUMENTS IN A FUNCTION   Xargs and XXargs

# def multiply(*numbers):   # xarg
#     total = 1
#     for number in numbers:
#         # total = total * number
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

#--------------------------

# def save_user(**user):    # ** allows the passing of multiple keyword arguments
#     print(user)  # can also use print(user["name"]) etc

# save_user(id=1, name="john", age=22)

# Output:
# {'id': 1, 'name': 'john', 'age': 22}


#------------------------------

# Scope refers to the region of the code where the variable is defined
# Global versus Local

# local variables in different functions can have the same name

#-------------------------------

# Exercise

#takes an input. If input is divisible by 3, returns "fizz". If divisible by 5, returns "buzz".  If divisible by both, return "fizzbuzz".

# def fizz_buzz(input):

#     if input % 3 == 0 and input % 5 != 0:
#         print("Fizz")
#     elif input % 5 == 0 and input % 3 != 0: 
#         print("Buzz")
#     elif input % 3 == 0 and input % 5 == 0:
#         print("Fizbuzz!!!")
#     else:
#         print(f"{input}")

# fizz_buzz(15)
# WORKS!


# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz!!"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input

# print(fizz_buzz(15))
# WORKS!!!