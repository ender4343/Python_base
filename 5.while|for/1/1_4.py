#На каждой итерации цикла пользователь вводит целое число. Цикл продолжается, пока не встретится число 0. Необходимо вычислить сумму введенных в цикле чисел и вывести результат на экран. Программу реализовать при помощи цикла while.
res=0
n=1
while n!=0:
    n=int(input())
    res+=n
print(res)