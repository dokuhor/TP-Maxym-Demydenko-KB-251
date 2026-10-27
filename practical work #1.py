def reverse_string(text):
    if len(text) != 10:
        raise ValueError("Рядок повинен містити рівно 10 символів")
    return text[::-1]


source_text = "abcdefg123"
result = reverse_string(source_text)

print("Початковий рядок:", source_text)
print("Результат:", result)
