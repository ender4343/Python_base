#Вводится натуральное число n. Вывести первое найденное натуральное число (то есть, перебирать числа, начиная с 1), квадрат которого больше значения n. Реализовать программу с использованием цикла while.
n=int(input())
i=1
while i<n:
    if i**2>n:
        print(i)
        break
    i+=1
#from math import ceil,sqrt
#n=int(input())
#res=ceil(sqrt(n))
#print(res)