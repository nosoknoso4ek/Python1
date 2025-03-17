# Функция для перевода числа из десятичной системы в другую систему счисления
def convert_base(n, base):
    digits = "0123456789ABCDEF"  # Цифры для систем счисления до 16
    result = ""
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    return result

# Ввод числа из консоли
input_data = input().strip()

# Проверка, что введено натуральное число
if not input_data.isdigit() or int(input_data) <= 0:
    print("Неверный ввод")
else:
    n = int(input_data)
    # Перевод в двоичную систему (основание 2)
    binary = convert_base(n, 2)
    # Перевод в восьмеричную систему (основание 8)
    octal = convert_base(n, 8)
    # Перевод в шестнадцатеричную систему (основание 16)
    hexadecimal = convert_base(n, 16)
    # Вывод результата
    print(f"{binary}, {octal}, {hexadecimal}")