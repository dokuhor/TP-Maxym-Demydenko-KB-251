def find_insert_position(sorted_list, new_value):
    position = 0

    while (
        position < len(sorted_list)
        and sorted_list[position] <= new_value
    ):
        position += 1

    return position


numbers = [1, 3, 5, 7, 9]

new_value = int(input("Введіть число для вставлення: "))
position = find_insert_position(numbers, new_value)

numbers.insert(position, new_value)

print("Позиція вставлення:", position)
print("Новий відсортований список:", numbers)
