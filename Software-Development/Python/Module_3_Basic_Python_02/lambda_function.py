# def double(x):
#     return x * 2

# this two lines function we can write in one line
# after lambda we will write parameter - one or two
# after colon you can write the result which we have written after return
doubled = lambda num : num * 2
squared = lambda num : num **2 # **2 it is called powered by 2 - we can do it also like - num * num
result = doubled(44)
result1 = squared(3)
print(result1)

# with many parameter
add = lambda a, b, c : a + b + c
resut_add = add(1, 2, 3)
print(resut_add)

# use of python map
numbers = [10, 20, 30, 40, 50, 60]
# we want to double each element in the array
# doubled_nums = map(doubled, numbers)
# if i directly print doubled_nums, it will return an address, but i can keep it in a list

doubled_nums = map(lambda x : x * 2, numbers) # here x is parameter and we will run this on numbers array
squared_nums = map(lambda x : x **2 , numbers)
print(list(doubled_nums))
print(list(squared_nums))

# list of dictionaly of actors
actors = [
   {'name': 'sabana', 'age': 51},
   {'name': 'sabnoor', 'age': 28},
   {'name': 'sabila noor', 'age': 30},
   {'name': 'srabontti', 'age': 26},
   {'name': 'shaon', 'age': 89},
]

juniors = filter(lambda x : x['age'] < 40, actors)
fibers = filter(lambda x : x ['age'] % 2 == 0, actors)
print(list(juniors))
print(list(fibers))
# there is a difference between Map and Filter
# - map will work on all without any condition
# - Filter - it will work on with condition