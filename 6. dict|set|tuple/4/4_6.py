#Пользователь с клавиатуры вводит названия городов, пока не введет букву q. Определить общее уникальное число городов, которые вводил пользователь. На экран вывести это число. Из коллекций при реализации программы использовать только множества.
st=set()
while True:
    n=input()
    if n=='q':break
    st.add(n)
print(len(st))