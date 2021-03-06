"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 79.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 24/03/2021
Дата последней модификации: 24/03/2021
Описание: Решение задачи 79 практикума № 1
#версия Python: 3.9
"""

"""
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
Разделить элементы каждого столбца матрицы на элемент этого столбца с наибольшим значением.
"""
import numpy as np 
N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
print(f'\nЗадан размер матрицы случайных целых чисел: [{N}, {M}]')
np.random.seed(0)
A = np.random.randint(10, size = (N, M))
print('\nПрямоугольная матрица случайных целых чисел:\n', A)
def get_column(A, index):
    column = []
    i = 0
    while i < len(A):
        column.append(A[i][index])
        i += 1
    return column
original_matrix = A.copy()
i = 0
while i < len(A):
    j = 0
    max_element = max(A[i])
    while j < len(A[i]):
        print(A[i][j], 'делим на ', max(get_column(A, j)))
        A[i][j] /= max(get_column(original_matrix, i))
        A[i][j] = round(A[i][j], 1)
        j += 1
    i += 1
print("\nМодифицированная матрица:\n", A)
