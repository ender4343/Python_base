#Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и, кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. Полученный результат должен возвращаться в виде строки.
from functools import wraps
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
def func_decor(chars="!?"):
    def show_translit(func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)
            res = ''.join([x if x not in chars else '-' for x in res])
            while '--' in res:
                res = res.replace('--', '-')
            return res
        return wrapper
    return show_translit

@func_decor("?!:;,. ")
def get_translit(s:str):
    return ''.join([t.get(x, x) for x in s.lower()])
print(get_translit(input()))