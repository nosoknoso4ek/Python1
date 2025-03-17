# Ввод доменного имени из консоли
domain = input().strip()

# Разделяем доменное имя по точкам
parts = []
current_part = ""
for char in domain:
    if char == '.':
        parts.append(current_part)
        current_part = ""
    else:
        current_part += char
parts.append(current_part)  # Добавляем последнюю часть

# Выводим части в обратном порядке
for i in range(len(parts) - 1, -1, -1):
    print(parts[i])