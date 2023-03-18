#В программе задана функция filter_lst (см. программу ниже), которая отбирает элементы, переданного ей итерируемого объекта и возвращает сформированный кортеж значений.
l1=lambda x:x<0
l2=lambda x:x>=0
l3=lambda x: 3<=x<=5
lst=list(map(int,input().split()))
def filter_lst(a,b=1):
    return a,b
print(*filter_lst(lst))
print(*filter_lst(lst,l1))
print(*filter_lst(lst,l2))
print(*filter_lst(lst,l3))
