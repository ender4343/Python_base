#Объявите функцию, которая принимает строку и заключает ее в указанный тег. Тег определяется формальным параметров tag с начальным значением в виде строки "h1". Например, мы передаем строку "Hello Python" и заключаем в тег "h1". На выходе должны получить строку (без кавычек):
def set_tag(s:str,tag:str="h1")->str:
    def close_tag(tag:str,flag:bool=1)->str:
        if flag:
            return "<"+tag+">"
        else:
            return "</"+tag+">"
    return close_tag(tag)+s+close_tag(tag,0)
s=input()
print(set_tag(s))
print(set_tag(s,"div"))