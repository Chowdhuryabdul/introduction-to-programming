# to return multiple from python
def multiple():
    return 3, 6
print(multiple())

things = 'pen', 'tripod', 'water bottole', 'charger', 'web cam',  'phone'
print(things)
print(type(things))

# to see what is in the first index
print(things[0])

# with negative index
print(things[-2])

# with slicing
print(things[2:4])

# to check thing exists
if 'phone' in things:
    print('YES')

# to print with the loop
for item in things:
    print(item)

# to set new item in the 0th  index, but it can not change as it is immutable
# things[0] = 'wagon'
# print(things)

# find how many items in tuple
print(len(things))

# declaring tuple with list
mega = ([1, 2, 3], [5, 6, 7, 8])
print(mega)
print(mega[0])
# change the list insdie tuple
mega[0][1] = 3333 #it will change in the 1st index of the 0th indx of tuple 
print(mega)