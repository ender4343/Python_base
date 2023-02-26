#Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне [2; n). Результат вывести на экран в строчку через пробел.
def is_simpl(dig):
    max_dev=int(round(dig**0.5))+1
    for i in range(2,max_dev):
        if dig%i==0:
            return False
    return True
n=int(input())
lst=[]
for i in range(2,n):
    if is_simpl(i):
        lst.append(i)
print(len(lst))