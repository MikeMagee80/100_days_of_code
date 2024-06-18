
# Display Even numbers between 1 and 10

# for x in range(1, 10):
#     while x % 2 == 0:
#         print(x)
#         break

# Output:
# 2
# 4
# 6
# 8

count = 0
for x in range(1, 10):
    while x % 2 == 0:
        count += 1
        print(x)
        break
print(f"We have {count} even numbers!")
