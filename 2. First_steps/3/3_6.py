# В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов. Максимальная вместимость каждого автобуса 20 человек. Допишите программу для вычисления минимального числа автобусов, необходимых для перевозки детей вместе с вожатыми. Результат выведите в консоль в виде целого числа.

n, m = map(int, input().split())
plc,p=20,n+m
res=round(p/plc)
print(res if p%plc==0 else res+1)
