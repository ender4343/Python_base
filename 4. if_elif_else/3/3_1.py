#Вводится два вещественных числа, каждое с новой строки. Необходимо с помощью тернарного условного оператора наибольшее значение присвоить переменной d и вывести ее на экран.
a=float(input())
b=float(input())
print(a if a>b else b)