#Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:
import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N_=int(input())
random.seed(1)
def get_randome_pswrd(N):
    yield ''.join((chars[random.randint(0,len(chars)-1)] for i in range(N)))

for i in range(5):
    print(next(get_randome_pswrd(N_)))