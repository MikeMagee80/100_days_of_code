
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# Output:
# 100
# 50
# 25
# 12
# 6
# 3
# 1


# command = ""
# while command.lower() != "quit":   #typing quit drops you out of the loop
#     command = input(">")
#     print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break