import math


"""
Вычислить и вывести на экран длину окружности и площадь круга одного 
и того же заданного радиуса R, который необходимо ввести 
с клавиатуры в сантиметрах. Результаты должны округляться до сотых.
"""
print('1 задача')
R = int(input())
print(round(2 * math.pi * R, 2))
print(round(math.pi * R ** 2, 2))

"""
Даны две переменные x = 10 и y = 55. 
Поменяйте их значения местами. 
Выведите значения переменных на экран до и после замены.
"""
print('2 задача')
x = 10
y = 55
print(x, y)
z = x
x = y
y = z
print(x, y)

"""
Вычислить и вывести на экран период колебания маятника 
длиной L с точностью до сотых. Для рассчетов использовать 
формулу T = 2π√(L/g), где g – ускорение свободного падения (9.81 м/c2). 
Значение длины маятника в метрах необходимо ввести с клавиатуры.
"""
print('3 задача')
L = int(input())
print(round(2 * math.pi * math.sqrt(L/9.81), 2))