"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 46.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 04/12/2020
Дата последней модификации: 04/12/2020
Описание: Решение задачи 46 практикума № 1
#версия Python: 3.8
"""

"""
Дан одномерный массив числовых значений, насчитывающий N элементов.
Дано положительное число T. Разделить это число между положительными элементами
массива пропорционально значениям этих элементов и добавить полученные доли
к соответствующим элементам.
"""
import random
N = int(input("Введите количество элементов массива: "))
T = int(input("Введите положительное число: "))
A = [random.randint(-100, 100) for i in range(N)]
print(A)
с = 0
for i in range(N):
    if A[i] > 0:
        с = с + A[i]
K = T/с
for i in range(N):
    if A[i] > 0:
        A[i] += (A[i]*K)
        
print(K)
print(A)
