#Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж. Необходимо создать еще один кортеж с уникальными (не повторяющимися) значениями из первого кортежа. Результат отобразите в виде списка чисел через пробел.
lst=list(map(int,input().split()))
tp=tuple()
for i in lst:
    if i not in tp:
        tp+=(i,)
print(tp)