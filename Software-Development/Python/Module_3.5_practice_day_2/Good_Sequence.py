n = int(input())
numbers = list(map(int, input(). split()))
empty_dictionary = {}
for i in numbers:
    if i in empty_dictionary:
        empty_dictionary[i] += 1
    else:
        empty_dictionary[i] = 1
removed_cnt = 0
for i in empty_dictionary:
    cnt = empty_dictionary[i]

    if cnt >= i:
        removed_cnt += cnt - i
    else: 
        removed_cnt += cnt
print(removed_cnt)



