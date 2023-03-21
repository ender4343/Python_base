#Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
s = input()
s_lst = s.split()
tp=tuple(map(lambda x: tuple(x.split()),s_lst))