my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]


#Первый вариант кода
i = 0
while i < len(my_list) and my_list[i] >= 0:
    if my_list[i] != 0:
        print(my_list[i])
    i += 1

#Второй вариант кода
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i += 1
        continue

    if my_list[i] < 0:
        break

    print(my_list[i])
    i += 1
