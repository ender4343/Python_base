#Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными. Вывести True, если это так и False - в противном случае.
lst=list(map(int,input().split()))
print(all(map(lambda x:x%2==0,lst)))