# Ввод длины стороны квадрата из консоли
side = float(input())  # Считываем число и преобразуем в float

# Вычисление периметра
perimeter = 4 * side

# Вычисление площади
area = side ** 2

# Вычисление диагонали (по теореме Пифагора)
diagonal = (side ** 2 + side ** 2) ** 0.5

# Округление результатов до двух знаков после запятой
perimeter_rounded = int(perimeter * 100) / 100
area_rounded = int(area * 100) / 100
diagonal_rounded = int(diagonal * 100) / 100

# Вывод результатов в требуемом формате
print(f"{perimeter_rounded:.2f}, {area_rounded:.2f}, {diagonal_rounded:.2f}")