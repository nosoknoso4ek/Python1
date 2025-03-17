def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Ввод данных
a, b = map(int, input().strip().split())

# Вызов функции и вывод результата
print(gcd(a, b))