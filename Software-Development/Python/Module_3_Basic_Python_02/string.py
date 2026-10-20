# string declaration
name = 'sakib\'s khan' #escape \
name2 = "sakin khan"
# multi line string
name3 = """
    Sakib khan 
    Number one
"""
print(name)

# string is a sequence of char
for char in name2:
    print(char)

# get the char of 3rd index
print(name2[3])

# slicing
print(name2[1:6])

# print h from the reveres side
print(name2[-3])

# total reverse printing
print(name2[::-1])


# change the 0th index letter from S to R
# name2[0] = 'R' 
print(name2)

# if sth in the string which we can find
if 'khan' in name2:
    print('exist')

# make all upper case
print(name2.upper())



# String is a sequence of charecter same as list. list is mutable and string is also immutable