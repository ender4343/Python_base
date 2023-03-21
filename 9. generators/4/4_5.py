# Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только корректно записанные адреса. Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания. А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
from string import ascii_letters,digits
def is_mail_corr(s:str):
    chars=set(ascii_letters+'@_.'+digits)
    if not set(s).issubset(chars):
        return False
    if s.index("@")>s.index("."):
        return False
    return True


ss=input().split()
res=filter(is_mail_corr,ss)
print(*res)

