numbers = [5, 2, 8]

numbers.extend([3, 1])
print("Після extend():", numbers)

numbers.append(10)
print("Після append():", numbers)

numbers.insert(1, 7)
print("Після insert():", numbers)

numbers.remove(7)
print("Після remove():", numbers)

numbers.sort()
print("Після sort():", numbers)

numbers_copy = numbers.copy()
print("Копія списку:", numbers_copy)

numbers.reverse()
print("Після reverse():", numbers)

numbers.clear()
print("Після clear():", numbers)
