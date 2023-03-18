#Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел, записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции. Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
def outer(tp:str="list"):
    if tp=="list":
        def outer(inp:str):
            return list(map(int,inp.split()))
    else:
        def outer(inp:str):
            return tuple(map(int,inp.split()))
    return outer
s1=input()
s2=input()
res=outer(s1)
print(res(s2))