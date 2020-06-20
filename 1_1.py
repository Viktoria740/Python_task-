name = input("Введите ваше имя:")
print(f"{name}, рады Вас видеть!")

age = int(input("сколько Вам полных лет?  "))
difference = int(18 - age)
if age < 18:
    print(f"только {age}:( Еще рано! Ждем тебя через {difference}лет!")
else:
    print("Добро пожаловать!")
