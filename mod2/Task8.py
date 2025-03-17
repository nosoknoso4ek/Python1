# Ввод списка слов (предположим, что слова вводятся через пробел)
input_data = input().strip()  # Считываем строку, например, "hello world python"

# Разделяем строку на слова (вручную, без использования split)
words = []
current_word = ""
for char in input_data:
    if char == ' ':
        if current_word:  # Если текущее слово не пустое
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word:  # Добавляем последнее слово, если оно есть
    words.append(current_word)

# Составляем новое слово из последних букв каждого слова
new_word = ""
for word in words:
    if word:  # Проверяем, что слово не пустое
        new_word += word[-1]  # Добавляем последнюю букву слова

# Вывод результата
print(new_word)