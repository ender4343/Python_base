#Объявите функцию для проверки числа на четность (возвращается True, если переданное число четное и False, если число нечетное).
def is_even(N):
    return N%2==0
while True:
    n=int(input())
    if n==1:break
    if is_even(n):
        print(n)