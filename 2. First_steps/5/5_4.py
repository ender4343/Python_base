#Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника. Напомню, что сумма длин двух произвольных сторон всегда должна быть больше третьей стороны. На экран вывести True, если треугольник формируется и False - в противном случае. Задача делается без использования условного оператора.
lst = list(map(int, input().split()))
lst.sort()
print(lst[2]<lst[1]+lst[0])