#Вводится натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером N x N элементов. Результат вывести на экран в виде таблицы чисел.

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n=int(input())
tp=(tuple(t[j][i]for i in range(n))for j in range(n))
for i in tp:
    print(*i)