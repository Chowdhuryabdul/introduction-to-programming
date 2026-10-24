text = (input())

# it will seperate the words with coma
words = text.split()

# take a list to append it
reversed_words = []

for word in words:
    reversed_words.append(word[::-1]) # here after reversing it will added to the list

# we need to use here join as previously use splilt by joinning it will remove the coma and join it
print(" ".join(reversed_words))