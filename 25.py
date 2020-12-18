"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 25.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи 25 практикума № 1
#версия Python: 3.8
"""

"""
Дано вещественное число A. Вычислить f(A), если f(x) = x^2 + 4x + 5, при x ≤ 2;
в противном случае f(x) = 1/(x^2 + 4x + 5).
"""
A = float(input("Введите число:"))
x=A
if x<=2:
    fx=x**2+4*x+5
    print("x<=2, f(A)=", fx)
else:
    fx=1/(x**2 + 4*x + 5)
    print("f(A)=", fx)
