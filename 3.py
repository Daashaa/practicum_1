"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: 3.py
Автор: 2020 © Д.П. Юткина, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: math
Описание: Решение задачи 3 практикума № 1
#версия Python: 3.8
"""

"""
Известны длины трёх сторон треугольника. Вычислить периметр треугольника и площадь по формуле Герона 
(указание: использовать модуль math и функцию sqrt ()).
"""
import math
a=2
b=4
c=3
p=(a+b+c)/2
print(p*2)
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(S)