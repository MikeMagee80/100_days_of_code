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

#VARIABLE NUMBER OF ARGUMENTS IN A FUNCTION

# def multiply(*numbers):   # xarg
#     total = 1
#     for number in numbers:
#         # total = total * number
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

#--------------------------

def save_user(**user):
    print(user)

save_user(id=1, name="john", age=22)

Output:
{'id': 1, 'name': 'john', 'age': 22}