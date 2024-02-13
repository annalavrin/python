#задание 1.1
""""
m = int(input("Введите число 1: "))
n = int(input("Введите число 2: "))
p = int(input("Введите число 3: "))

count_negative = 0


if m < 0:
    count_negative += 1
if n < 0:
    count_negative += 1
if p < 0:
    count_negative += 1

print("Количество отрицательных чисел: ", count_negative)
"""
#задание 1.16
"""
number = int(input("Введите число от 0 до 7: "))

if number == 0:
    print("Ноль")
elif number == 1:
    print("Один")
elif number == 2:
    print("Два")
elif number == 3:
    print("Три")
elif number == 4:
    print("Четыре")
elif number == 5:
    print("Пять")
elif number == 6:
    print("Шесть")
elif number == 7:
    print("Семь")
else:
    print("Введено недопустимое число")
"""
#задание 3 Сформировать одномерный список целых чисел A,
# используя генератор случайных чисел (диапазон от 0 до 99). Размер списка n ввести с клавиатуры.

import random

n = int(input("Введите размер списка: "))

A = [random.randint(0, 99) for _ in range(n)]

print("Сформированный список A:", A)

##A = A: [96, 1, 1, 17, 56]  # Пример исходного списка A
"""
##задание 3.2.Все четные по значению элементы исходного списка A поместить в новый список B.

B = []  # Создаем пустой список B

# Проходим по каждому элементу списка A и добавляем четные элементы в список B
for element in A:
    if element % 2 == 0:  # Проверяем, является ли элемент четным
        B.append(element)  # Добавляем четный элемент в список B

print("Список A:", A)
print("Список B (четные элементы из A):", B)
"""

##задание 3.15
# удалить  элементы из списка A, у которых индексы кратны 3
B = [element for index, element in enumerate(A) if index % 3 != 0]

print("Сформированный список B:",B) # выводим обновленный список A