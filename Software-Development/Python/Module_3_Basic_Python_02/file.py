# how to open a file
# to whom we will open, we have to give a name of file
# after that i need to give a text mode. actually what i want to do read, write or anything else
with open('message.txt', 'w') as file:
    file.write('I love you, Python')

# By runnning this it will open a new file 

# bby this it will write this in the message.txt file - here a means append
with open('message.txt', 'a') as file:
    file.write('I love you, Sadia')

# Now er read - those we have writte and append now we can read it in terminal
with open('message.txt', 'r') as file:
    text = file.read()
    print(text)