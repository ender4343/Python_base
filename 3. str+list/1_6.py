#С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
l1,l2=input().split()
print(f"Коды: {l1} = {str(ord(l1))}, {l2} = {str(ord(l2))}")