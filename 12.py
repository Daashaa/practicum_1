"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 12.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 16/11/2020
Дата последней модификации: 16/11/2020
Описание: Решение задачи 12 практикума № 1
#версия Python: 3.8
"""

"""
Дано вещественное число.
Определить, какое это число: положительное, отрицательное, ноль.
"""
N = float (input("Введите вещественное число:"))
if (N > 0):
    print("Число положительное")
elif (N == 0):
    print("Число равно 0")
else:
    print("Число отрицательное")
