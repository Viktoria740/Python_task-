def numb(n_1, n_2):
    try:
        return round(n_1 / n_2, 3)
    except ZeroDivisionError:
        return "На 0 делить нельзя :Р"
    except TypeError:
        return "Упс! мы же математикой занимаемся! прошу ввести число!"
    except ValueError:
        return "Упс! прошу ввести число!"


print(numb(int(input("число 1: ")), int(input("число 2: "))))
