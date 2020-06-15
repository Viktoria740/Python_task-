money = float(input("сумма выручки за прошедший месяц:"))
spend = float(input("сумма расходов за прошедший месяц:"))
profit = (money-spend)/money
if money > spend:
    print(f"хороший результат! Ваша компания работает в плюс! Рентабельность компании составляет {profit:.2f}")
    empl = int(input("укажите количество сотрудников фирмы:"))
    profit_per_one_emp = ((money - spend) / empl)
    print(f"прибыль фирмы в расчете на одного сотрудника={profit_per_one_emp:.2f}")
elif money == spend:
    print("увы! сработали в ноль!")

else:
    print("к сожалению, в этом месяце компания отработала в минус.")
