# Ввод номера телефона из консоли
phone_number = input().strip()

# Создаем новую строку, содержащую только цифры и знак '+'
cleaned_number = ""
for char in phone_number:
    if char.isdigit() or char == '+':  # Оставляем только цифры и '+'
        cleaned_number += char

# Вывод очищенного номера
print(cleaned_number)