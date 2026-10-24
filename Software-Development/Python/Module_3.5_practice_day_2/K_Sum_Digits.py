n = int(input())

# we can take input by this way from list
# numbers = list(map(int, input(). split()))

# taking digit as input - this number comes as string
numbers = input()
# print(type(numbers))


# sum = 0
# print(numbers)
# for i in numbers:
#     sum = sum + int(i)
# print(sum)

# we can do it. with map to convert all the digit into int
# numbers = map(int, numbers)
# print(sum(numbers))

# we can do it one line
print(sum(map(int, numbers)))