n = int(input())
numbers = list(map(int, input().split()))
reversed_number = numbers[::-1]

if numbers == reversed_number:
    print("YES")
else:
    print("NO")


# if we have single number -
# than we can convert the number into str and than reversed it.
# but here it is list