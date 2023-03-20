#Объявите функцию для проверки числа на нечетность (возвращается True, если переданное число нечетное и False, если число четное). 
def is_odd(N):
    return N%2!=0
lst=[x for x in list(map(int,input().split()))if is_odd(x)]
print(sorted(lst))