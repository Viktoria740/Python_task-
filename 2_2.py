
a = input('Введите элементы для массива разделяя их пробелами: ').split()
i = 0
while i + 1 < len(a):
    if i % 2 == 0:
        a.insert(i, a.pop(i + 1))
    i += 1
print(f'Измененный список {a}')


