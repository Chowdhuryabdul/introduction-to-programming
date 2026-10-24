n, q = map(int, input().split())
numbers = list(map(int, input().split()))
prefix = [0]
for num in numbers:
    prefix.append(prefix[-1] + num)

for i in range(q):
    a, b = map(int, input().split())
    total = prefix[b] - prefix[a - 1]

    print(total)


