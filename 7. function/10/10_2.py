#Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего аргумента на некоторую величину n - параметр внешней функции с сигнатурой:
def counter_add(n):
    def add_num(num):
        nonlocal n
        return n+num
    return add_num
k=int(input())
cnt=counter_add(2)
print(cnt(k))