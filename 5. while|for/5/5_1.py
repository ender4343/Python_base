#Вводится список городов в одну строчку через пробел. Необходимо создать итератор для этого списка и с помощью итератора вывести на экран в столбик первые два значения (названия городов).
lst=input().split()
it=iter(lst)
lst_out=(next(it),next(it))
print(*lst_out,sep='\n')