#Гражданин 1 января открыл счет в банке, вложив 1000 руб. Каждый год размер вклада увеличивается на 5% от имеющейся суммы. Определить сумму вклада через n лет (n - целое положительное число, вводимое с клавиатуры). Результат округлить до сотых и вывести на экран. Программу реализовать при помощи цикла while.
t=int(input())
money=1000
i=0
while i!=t:
    money*=1.05
    i+=1
money=round(money,2)
print(money)