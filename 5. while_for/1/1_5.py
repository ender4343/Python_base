#Вводится строка (слаг). Замените в этой строке все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-). Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.
s=input()
while "--" in s:
    s=s.replace("--",'-')
print(s)