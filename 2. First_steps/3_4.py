#Допишите текст программы для вычисления евклидового расстояния (гипотенузы) по перемещениям a и b (формула: ). Округлите результат с точностью до сотых. Полученное значение выведите на экран.
import math as m

a,b=map(int,input().split())
print(round(m.sqrt(a**2+b**2),2))