#Необходимо определить, можно ли первое число нацело разделить на второе. На экран вывести True, если делится и False - в противном случае. Задача делается без использования условного оператора.
a, b = map(int, input().split())
res=a%b==0
print(res)