"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 29.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 30/11/2020
Дата последней модификации: 30/11/2020
Описание: Решение задачи 29 практикума № 1
#версия Python: 3.8
"""

"""
Известен ГОД. Определить, будет ли этот год високосным, и к какому веку этот год относится
"""
X = int(input("Введите год:"))
if (X % 4 == 0 and X % 100 != 0) or (X % 400 == 0):
    print("Год невисокосный")
else:
    print("Год високосный")
if X % 100 == 0:
    X = X // 100
    print(X," век")
elif X % 100 != 0:
    X = (X // 100) + 1
    print(X," век")
