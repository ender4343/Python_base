#Вводится строка. Нужно создать итератор для перебора символов этой строки. Затем, перебрать через созданный итератор все символы до первого пробела. В процессе перебора символы выводить на экран в одну строчку друг за другом (без пробелов). Гарантируется, что во введенной строке имеется хотя бы один пробел.
s=input()
res=''
it=iter(s)
while True:
    k=next(it)
    if k==" ":
        break
    res+=k
print(res)