#Из модуля random импортируйте только две функции: seed и random, но у последней должен быть синоним rnd (имя, через которое она будет вызываться в программе). Выполните в программе эти функции, следующим образом:
from random import seed
from random import random as rnd
seed(10)
print(round(rnd(), 2))