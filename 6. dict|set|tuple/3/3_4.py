#Вводятся имена студентов в одну строчку через пробел. На их основе формируется кортеж. Отобразите на экране все имена из этого кортежа, которые содержат фрагмент "ва" (без учета регистра). Имена выводятся в одну строчку через пробел в нижнем регистре (малыми буквами).
tp=tuple(input().split())
letr='ра'
for i in tp:
    i=i.lower()
    if letr in i:
        print(i,end=" ")