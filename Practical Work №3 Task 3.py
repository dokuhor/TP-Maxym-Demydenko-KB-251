def dodaty(a, b):
    return a + b


def vidniaty(a, b):
    return a - b


def pomnozhyty(a, b):
    return a * b


def podilyty(a, b):
    if b == 0:
        return None
    return a / b


pershe_chyslo = float(input("Введіть перше число: "))
diia = input("Введіть дію (+, -, *, /): ")
druhe_chyslo = float(input("Введіть друге число: "))

match diia:
    case "+":
        rezultat = dodaty(pershe_chyslo, druhe_chyslo)
    case "-":
        rezultat = vidniaty(pershe_chyslo, druhe_chyslo)
    case "*":
        rezultat = pomnozhyty(pershe_chyslo, druhe_chyslo)
    case "/":
        rezultat = podilyty(pershe_chyslo, druhe_chyslo)
    case _:
        rezultat = "Невідома дія"

if rezultat is None:
    print("На нуль ділити не можна.")
else:
    print("Результат:", rezultat)
