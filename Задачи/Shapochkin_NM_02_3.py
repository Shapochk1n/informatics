"""
Вычислить и вывести на экран сумму кубов натуральных чисел 
от 1 до n включительно. Верхний предел должен вводиться 
с клавиатуры и не должен превышать числа 100.
"""
print('1 задача')
n = int(input())
if n > 100:
    print('n не должен превышать числа 100')
else:
    s = 0
    for i in range(1, n+1):
        s = s + i ** 3
    print(s)

"""
Выведите на экран таблицу умножения чисел от одного до девяти.
"""
print('2 задача')
for i in range(1, 10):
    l = []
    for j in range(1, 10):
        l.append(j * i)
    print(l)