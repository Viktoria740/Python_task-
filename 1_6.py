start = int(input("Старт! С какого расстояния начнем?-"))
finish = int(input("К какой цели движемся? - "))
day = 1
if start <= 0 or finish < start or finish < 0 :
    print("не надо недооценивать себя! введите положительное значение ;)")
else:
    while start <= finish:
        start += start * 0.1
        day += 1

    print(f"Цель далека, пока не начал бежать! старт! ты достигнешь результата на {day} день")
