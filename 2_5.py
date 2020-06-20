my_list = [8, 7, 7, 4, 3, 3, 3, 2]
new_number = int(input("Введите элемент рейтинга: "))
i = 0
for n in my_list:
    if new_number <= n or new_number > 0:
        i += 1
        my_list.insert(i, new_number)
        print(my_list)
        break
else:
    print("Проверьте введенные данные, число должно быть положительным")
