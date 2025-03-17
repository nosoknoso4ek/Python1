def check_numbers(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) == 1:
        print("Все числа равны")
    elif len(unique_numbers) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

# Пример использования
input_data = input().strip().split()
numbers = list(map(int, input_data))
check_numbers(numbers)