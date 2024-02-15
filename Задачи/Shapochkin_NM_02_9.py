import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

"""
Для каждой задачи необходимо:

Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций), 
график каждой функции должен быть одного цвета для одного значения α и β.
Подписать оси и заголовок
Создать легенду
Сохранить изображение в svg файл
"""
dir = os.getcwd()

const = [[1, 1],
        [2, 1],
        [1, 2]]

"""
Построить в общих осях графики для:
α=1,β=1
α=2,β=1
α=1,β=2
"""
def f(x, a, b):
    return (x**b + a**b) / x**b

x = np.linspace(-1, 10, 100)

for i in range(len(const)):
    plt.plot(x, f(x, const[i][0], const[i][1]), color='red', label='график')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.legend()
    plt.show()
    plt.savefig(dir + f'/chart{i+1}.svg')

"""
остроить в общих осях графики для x>0.
На том же графике сделать 2 врезки, демонстрирующие поведение графиков на 2 интервалах:

для малых x
для больших x
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций.

Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.
"""

def f_above_zero(x, a, b):
    if x > 0:
        return (x**b + a**b) / x**b

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(10, 6))
fig.subplots_adjust(left=0.2, bottom=0.2)

def graph(a, b, ax):
    x = np.linspace(-5, 5, 200)
    y = [f_above_zero(x_, a, b) for x_ in x]

    # create graph
    ax.plot(x, y, color='red', label='график при x>0')
    ax.set_title(f'a={a}, b={b}')
    ax.axhline(y=1)
    ax.axvline(x=0)
    plt.ylabel('y')
    plt.xlabel('x')
    ax.legend()

    # small x values
    axins1 = inset_axes(ax, width="20%", height="20%", 
                        loc=2, borderpad=4)
    x = np.linspace(0, 0.1, 100)
    y = [f_above_zero(x_, a, b) for x_ in x]
    axins1.plot(x, y, color='red', label='график')
    axins1.set_title('small x values')

    # big x values
    axins2 = inset_axes(ax, width="20%", height="20%", 
                        loc=3, borderpad=4)
    x = np.linspace(100, 1000, 100)
    y = [f_above_zero(x_, a, b) for x_ in x]
    axins2.plot(x, y, color='red', label='график')
    axins2.set_title('big x values')

for i in range(len(const)):
    graph(const[i][0], const[i][1], (ax1, ax2, ax3)[i])

plt.show()
plt.savefig(dir + '/chart4.svg')

"""
Построить в общих осях графики для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков 
при удалении x от 0 к −∞.

Необходимо продемонстрировать возможность (или невозможность) 
пересечений и стремление функций. Так же нанесите на графики прямую f(x) = 0.

Цвет линий на врезках и основном графике должен быть 
одинаковым для одних и тех же значений α и β.
"""
def f_below_zero(x, a, b):
    if x < 0:
        return (x**b + a**b) / x**b

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(10, 6))
fig.subplots_adjust(left=0.2, bottom=0.2)

def graph(a, b, ax):
    x = np.linspace(-50, 0, 400)
    y = [f_below_zero(x_, a, b) for x_ in x]

    # create graph
    ax.plot(x, y, color='red', label='график при x<0')
    ax.set_title(f'a={a}, b={b}')
    ax.axhline(y=1)
    ax.axvline(x=0)
    plt.ylabel('y')
    plt.xlabel('x')
    ax.legend()

    # small x values
    axins1 = inset_axes(ax, width="20%", height="20%", 
                        loc=2, borderpad=5)
    x = np.linspace(-0.1, 0, 100)
    y = [f_below_zero(x_, a, b) for x_ in x]
    axins1.plot(x, y, color='red', label='график')
    axins1.set_title('small x values')

    # big x values
    axins2 = inset_axes(ax, width="20%", height="20%", 
                        loc=3, borderpad=5)
    x = np.linspace(-400, -300, 100)
    y = [f_below_zero(x_, a, b) for x_ in x]
    print(x, y)
    axins2.plot(x, y, color='red', label='график')
    axins2.set_title('big x values')

for i in range(len(const)):
    graph(const[i][0], const[i][1], (ax1, ax2, ax3)[i])

plt.show()
plt.savefig(dir + '/chart5.svg')

"""
Построить в общих осях графики для:
α=1,β=0.5
α=1,β=−0.5
α=1,β=−1.5
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость
"""
const = [[1, 0.5],
        [1, -0.5],
        [1, -1.5]]

def d_f(x, a, b):
    h = 1e-5
    return (f(x+h, a, b)-f(x-h, a, b))/(2*h)

def double_d_f(x, a, b):
    h = 1e-5
    return (d_f(x+h, a, b)-d_f(x-h, a, b))/(2*h)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(10, 6))
fig.subplots_adjust(left=0.2, bottom=0.2)

def graph(a, b, ax):
    # у первого графика вторая производная при малых x дает большие значения, 
    # из-за чего масштаб становится слишком большим, поэтому x считаем от 0.5
    x = np.linspace(0.5, 5, 200)
    y = [f(x_, a, b) for x_ in x]
    d_y = [d_f(x_, a, b) for x_ in x] # производная
    double_d_y = [double_d_f(x_, a, b) for x_ in x] # двойная производная
    # create graph
    ax.plot(x, y, color='red', label='график функции')
    ax.set_title(f'a={a}, b={b}')
    ax.axhline(y=0)
    ax.axvline(x=0)
    plt.ylabel('y')
    plt.xlabel('x')
    # create derivatives
    ax.plot(x, d_y, color='black', label='производная')
    ax.plot(x, double_d_y, color='green', label='двойная производная')

    ax.legend()

for i in range(len(const)):
    graph(const[i][0], const[i][1], (ax1, ax2, ax3)[i])
plt.show()
plt.savefig(dir + '/chart6.svg')

"""
В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с α=1 проходят через общую точку (1, 2).
Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.
Каждый график будет содержать 4 кривые. 2 общих:
α=1,β=0 (в качестве цвета попробуйте использовать 'b--')
α=1,β=−1 (в качестве цвета попробуйте использовать 'r--')
И по 2 уникальных для каждого графика:
α=1,β=0.5 и
α=1,β=0.8
α=1,β=−0.5 и
α=1,β=−0.8
α=1,β=−1.5 и
α=1,β=−2.5
Не забудьте добавить легенду на каждый график. Для этого может потребоваться вызвать метод legend() для каждого объекта осей.
"""
const = [
        [
        [1, 0.5],
        [1, 0.8],
        [1, -0.9],
        [1, 1.1]
        ],
        [
        [1, -0.5],
        [1, -0.8],
        [1, 0.6],
        [1, 0.2]
        ],
        [
        [1, -1.5],
        [1, -2.5],
        [1, 0.9],
        [1, 1.3]
        ]
        ]

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(10, 6))
fig.subplots_adjust(left=0.2, bottom=0.2)

def graph(a, b, ax):
    x = np.linspace(0, 5, 200)
    y = [f(x_, a, b) for x_ in x]
    # create graph
    ax.plot(x, y, color='red', label=f'a={a}, b={b}')
    ax.set_title(f'графики функции')
    ax.axhline(y=0)
    ax.axvline(x=0)
    plt.ylabel('y')
    plt.xlabel('x')

    ax.legend()

for i in range(len((ax1, ax2, ax3))):
    for j in range(len(const[0])):
        graph(const[i][j][0], const[i][j][1], (ax1, ax2, ax3)[i])

    dot_x = np.linspace(1, 1, 1)
    dot_y = [f(x_, const[0][0][0], const[0][0][1]) for x_ in dot_x]
    (ax1, ax2, ax3)[i].scatter(dot_x, dot_y, color='green', label='точка пересечения')
    (ax1, ax2, ax3)[i].legend()

plt.show()
plt.savefig(dir + '/chart7.svg')