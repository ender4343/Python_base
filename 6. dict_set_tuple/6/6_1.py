#Первая цифра - это числовое значение первой оценки. Остальные оценки имеют возрастающие на 1 числа. С помощью генератора словарей необходимо сформировать словарь d, где ключами будут выступать числа, а значениями - слова.
lst_in=list(input().split())
i=int(lst_in[0])
d={(i+j-1):lst_in[j] for j in range(1,len(lst_in))}
print(d[4])