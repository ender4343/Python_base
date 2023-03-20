#Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру
#Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
def get_sq(width, height):
    return width*height
def func_show(func):
    def inner(*args):
        res1=func(*args)
        print(f'Площадь прямоугольника: {res1}')
    return inner
a=tuple(map(int,input().split()))
res=func_show(get_sq)
res(a[0],a[1])
