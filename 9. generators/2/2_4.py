
#задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru

import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase
N_=int(input())
random.seed(1)
def get_randome_mail(N):
    yield ''.join((chars[random.randint(0,len(chars)-1)] for i in range(N)))+'@mail.ru'

for i in range(5):
    print(next(get_randome_mail(N_)))