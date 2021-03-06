"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 27.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи 27 практикума № 1
#версия Python: 3.8
"""

"""
Дано вещественное число A. Вычислить f(A), если f(x) = 0 при x ≤ 0; f(x) = x^2 − x при 0 < x < 1,
в противном случае f(x) = x^2 − sin(πx^2).
"""
import math
A = float(input("Введите число А:"))
x = A
if x <= 0:
    fx = 0
    print("x <= 0; f(A) =:", fx)
elif 0 < x < 1:
    fx = x**2 - x
    print("0 < x < 1; f(A) =:", fx)
else:
    fx = math.pow(x, 2) - math.sin((math.pi * math.pow(x, 2)))
    print("x >= 1; f(A) =:", fx)
