#вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
#Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
#Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
from functools import wraps
def outer(start=5):
    def midle(func):
        @wraps
        def inner(*args):
            return func(*args)+start
        return inner
    return midle

@outer()
def get_summ(s:str):
    return sum([int(i) for i in s.split()])

s=input()

print(get_summ(s))