#(На использование цикла while). Вводятся названия книг (каждое с новой строки). Удалить из введенного списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом). Результат вывести на экран в виде строки из оставшихся названий через пробел.

#['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
lst=[i for i in lst_in if ' 'not in i]
print(*lst)