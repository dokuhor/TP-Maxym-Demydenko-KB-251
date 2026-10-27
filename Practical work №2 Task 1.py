from math import sqrt


def obchyslyty_dyskryminant(a, b, c):
    return b ** 2 - 4 * a * c


def znayty_koreni(a, b, c):
    if a == 0:
        print("Коефіцієнт a не може дорівнювати нулю.")
        return

    dyskryminant = obchyslyty_dyskryminant(a, b, c)

    if dyskryminant > 0:
        x1 = (-b + sqrt(dyskryminant)) / (2 * a)
        x2 = (-b - sqrt(dyskryminant)) / (2 * a)
        print("Рівняння має два корені:", x1, "і", x2)
    elif dyskryminant == 0:
        x = -b / (2 * a)
        print("Рівняння має один корінь:", x)
    else:
        print("Рівняння не має дійсних коренів.")


a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

znayty_koreni(a, b, c)
