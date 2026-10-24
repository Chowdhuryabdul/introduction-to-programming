n = int(input())
numbers = list(map(int, input().split()))

# reversed = numbers[::-1]
# print(reversed)

# find min and max
min_value = min(numbers)
max_value = max(numbers)

# find index
min_index = numbers.index(min_value)
max_index = numbers.index(max_value)

# swap between min and max
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)