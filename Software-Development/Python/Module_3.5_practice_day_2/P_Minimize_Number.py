n = int(input())
numbers = list(map(int, input(). split()))
cnt_operation = 0
while True:
    odd_nmbr = False

    for number in numbers:
        if number % 2 != 0:
            odd_nmbr = True
            break
    if odd_nmbr:
        break
    for i in range(n):
        numbers[i] = numbers[i] // 2
        
    cnt_operation += 1

       
print(cnt_operation)