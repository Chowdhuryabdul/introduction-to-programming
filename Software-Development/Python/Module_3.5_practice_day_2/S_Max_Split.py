s = input()
# print(s)

L_cnt = 0
R_cnt = 0
empty_string = ""
blnc_prt = []

for char in s:
    empty_string += char
    # print(empty_string)

    if char == "L":
        L_cnt += 1
    else:
        R_cnt += 1

    if L_cnt == R_cnt:
        blnc_prt.append(empty_string)
        empty_string = ""
        # print(empty_string)
print(len(blnc_prt))

for s_prt in blnc_prt:
    print(s_prt)
