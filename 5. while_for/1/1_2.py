#Вводится стоимость одной книги x рублей (вещественное число). Необходимо вывести на экран в строчку через пробел стоимости 2, 3, ... 10 таких книг с точностью до десятых. Программу реализовать при помощи цикла while.
coast=float(input())
n=2
lst=[]
while n<11:
    lst.append(round(n*coast,1))
    n+=1
print(*lst)