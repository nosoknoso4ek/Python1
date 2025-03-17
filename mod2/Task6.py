# Ввод строки из консоли
s = input().strip()

# Счетчики для нулей и единиц
count_zero = 0
count_one = 0

# Подсчет нулей и единиц
for char in s:
    if char == '0':
        count_zero += 1
    elif char == '1':
        count_one += 1

# Сравнение количества нулей и единиц
if count_zero == count_one:
    print("yes")
else:
    print("no")