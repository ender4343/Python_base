#Вводятся два вещественных числа в одну строку через пробел. Вывести на экран наибольшее из чисел. Задачу решить с помощью условного оператора.
a,b=map(float,input().split())
print(a if a>b else b)