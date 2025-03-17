def can_form_palindrome(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return odd_count <= 1

def build_palindrome(s):
    if not can_form_palindrome(s):
        return "Нельзя составить палиндром"
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    left_half = ""
    middle_char = ""
    for char, count in sorted(char_count.items()):
        if count % 2 != 0:
            middle_char = char
        left_half += char * (count // 2)
    return left_half + middle_char + left_half[::-1]

# Ввод данных
s = input().strip()

# Вызов функции и вывод результата
print(build_palindrome(s))