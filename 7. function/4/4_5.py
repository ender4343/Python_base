#Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением True. Если параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными буквами, а иначе - малыми.
def set_tag(s:str,tag:str="h1",up:bool=1)->str:
    def close_tag(tag:str,flag:bool=1)->str:
        if flag:
            return "<"+tag+">"
        else:
            return "</"+tag+">"
    if up:
        return close_tag(tag).upper()+s+close_tag(tag,0).upper()
    else:
        return close_tag(tag)+s+close_tag(tag,0)
s=input()

print(set_tag(s,"div"))
print(set_tag(s,"div",0))