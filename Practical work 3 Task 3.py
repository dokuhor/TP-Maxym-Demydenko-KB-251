student = {
    "ім'я": "Максим",
    "спеціальність": "Кібербезпека",
    "курс": 1
}

student.update({"місто": "Чернігів"})
print("Після update():", student)

del student["курс"]
print("Після del:", student)

print("Ключі:", list(student.keys()))
print("Значення:", list(student.values()))
print("Пари ключ-значення:", list(student.items()))

student.clear()
print("Після clear():", student)
