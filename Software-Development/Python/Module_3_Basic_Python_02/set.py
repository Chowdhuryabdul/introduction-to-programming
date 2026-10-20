# set : set is an collection of unique items - it will not any duplicate values

numbers = [12, 34, 65, 67, 65, 98, 4, 98]
print(numbers)

# use of set
numbers_set = set(numbers)
print(numbers_set)

# add new element
numbers_set.add(33)
print(numbers_set)

# to remove an element
numbers_set.remove(65)
print(numbers_set)

# run a loop
for item in numbers_set:
    print(item)

if 34 in numbers_set:
    print("YES")


# how to uion in set
A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B) # it will print the common 1 3 5 in both set
print(A | B) # it means AUB - it will print the element both have in total 1 2 3 4 5 7
# list --> []
# tuple --> ()
# set --> {}