"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 49.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 04/12/2020
Дата последней модификации: 04/12/2020
Описание: Решение задачи 49 практикума № 1
#версия Python: 3.8
"""

"""
Дан одномерный массив числовых значений, насчитывающий N элементов.
Определить, имеются ли в массиве два подряд идущих нуля.
"""
import random
N = int(input("Введите количество элементов массива: "))
A = [random.randint(-5, 5) for i in range(N)]
print(A)
for i in range(N):
    x=0
    if A[i] == 0 and A[i-1] == 0:
        x+=1
if x>0:
    print("В массиве имеются два подряд идущих нуля")
else:
    print("В массиве нет нулей идущих подряд")
