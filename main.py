"""number = int(input("Ввод данных: "))
if number == 6 or number == 7:
    print("Выходной!")
else:
    print("Не выходной.")"""


x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))


if x == 0 and y == 0:
    print()
elif x > 0 and y > 0:
    print(f'При координатах x = {x} и y = {y} точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print(f'При координатах x = {x} и y = {y} точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(f'При координатах x = {x} и y = {y} точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print( f'При координатах x = {x} и y = {y} точка находится в плоскости 4 ')




'''
ax = float(input('Введите координаты точки a по оси x:'))
ay = float(input('Введите координаты точки a по оси y:'))
bx = float(input('Введите координаты точки b по оси x:'))
by = float(input('Введите координаты точки b по оси y:'))

import math
distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(distans)'''