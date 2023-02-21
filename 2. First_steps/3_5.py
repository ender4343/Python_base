#Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе), используя формулу ., где . Выведите результат в консоль в виде целого числа с помощью функции print.

import math as m


n, k = map(int, input().split())
res=round((m.factorial(n))/(m.factorial(k)*m.factorial(n-k)))
print(res)