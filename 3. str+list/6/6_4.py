#Необходимо вычислить средний балл и вывести его на экран с точностью до десятых (один знак после запятой).

marks=list(map(int,input().split()))
res=sum(marks)/len(marks)
print(round(res,1))