#водится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее к прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел
lst_in=['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
res=zip(*zip(*[[int(i)for i in j.split()]for j in lst_in]))
for i in res:
    print(*i)