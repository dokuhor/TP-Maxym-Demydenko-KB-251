def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


while True:
    operation = input(
        "Введіть дію (+, -, *, /) або «вихід» для завершення: "
    ).strip().lower()

    if operation == "вихід":
        print("Програму завершено.")
        break

    if operation not in ("+", "-", "*", "/"):
        print("Невідома дія. Спробуйте ще раз.")
        continue

    try:
        first_number = float(input("Введіть перше число: "))
        second_number = float(input("Введіть друге число: "))
    except ValueError:
        print("Потрібно ввести числа.")
        continue

    if operation == "+":
        result = add(first_number, second_number)
    elif operation == "-":
        result = subtract(first_number, second_number)
    elif operation == "*":
        result = multiply(first_number, second_number)
    else:
        result = divide(first_number, second_number)

    if result is None:
        print("На нуль ділити не можна.")
    else:
        print("Результат:", result)
