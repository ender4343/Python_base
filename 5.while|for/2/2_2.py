#На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных чисел, до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue, а также использовать цикл while. Результат произведения вывести на экран.
res=1
i=1
while i!=0:
    i=int(input())
    if i<=0:
        continue
    res*=i
print(res)
    