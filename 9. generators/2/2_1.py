#Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum, которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. 
N=int(input())
def get_sum():
    i=1
    while i!=N+1:
        yield sum(range(1,i+1))
        i+=1
    i=1

print(*list(get_sum()))