#Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами). 
#Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат
def func_decor(tag='h1'):
    def outer(func):
        def inner(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return inner
    return outer


@func_decor(tag='div')
def get_lowwer(s:str):
    return s.lower()
print(get_lowwer(input()))


