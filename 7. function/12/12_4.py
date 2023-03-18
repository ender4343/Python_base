#Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
#Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps (не забудьте сделать импорт: from functools import wraps). Такое декорирование необходимо, чтобы исходная функция get_list сохраняла свои локальные свойства: __name__ и __doc__.
from functools import wraps


def func_decor(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))
    return wrapper


@func_decor
def get_list(s:str):
    '''Функция для формирования списка целых значений'''
    return [int(i)for i in s.split()]
