#Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s (s - строка, параметр внутренней функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции. 
def outer(tag:str):
    def inner(s:str):
        nonlocal tag
        return f"<{tag}>{s}</{tag}>"
    return inner
tag=input()
s=input()
res=outer(tag)
print(res(s))