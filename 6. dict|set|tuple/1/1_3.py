#Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать словарь, затем проверить, существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки). Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
flag=True
to_cheek=['house', 'True' , '5' ]
s=input().split()
d={}
for i in s:
    x,y=i.split('=')
    d[x]=y
for i in to_cheek:
    if i not in (d):
        flag=False
print("ДА"if flag else'НЕТ')


