#Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть, отрицательные числа нужно делать положительными). Вызовите эту функцию для введенного числа x:
get_abs=lambda x: abs(x)
x=float(input())
print(get_abs(x))