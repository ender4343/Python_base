#Вводится последовательность целых чисел в одну строчку через пробел. Необходимо их добавить в кортеж t. Результат вывести на экран командой:

t = (3.4, -56.7)
tp=tuple(map(int,input().split()))
res=t+tp
print(res)