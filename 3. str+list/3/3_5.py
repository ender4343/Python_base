#Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку. Для двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали по три цифры. Вывести на экран полученные числа в столбик.
print(*map(lambda x:x.rjust(3,"0"),input().split()),sep="\n")