#Вводится натуральное (то есть, целое положительное) число (от трехзначного и более). Найти произведение всех его цифр. Результат вывести на экран. Программу реализовать при помощи цикла while.
x=input()
res=1
i=0
N=len(x)
while i<N:
    res*=int(x[i])
    i+=1
print(res)
