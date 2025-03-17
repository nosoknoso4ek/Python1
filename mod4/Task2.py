def fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:  # Если степень чётная
        return fast_pow(a * a, n // 2)
    else:  # Если степень нечётная
        return a * fast_pow(a, n - 1)

# Ввод данных
a, n = map(int, input().strip().split())

# Вызов функции и вывод результата
print(fast_pow(a, n))