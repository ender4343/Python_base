#Запишите функцию без аргументов, которая считывает с клавиатуры имя и фамилию, записанные в одну строку через пробел, и выводит на экран сообщение (без кавычек):
def say_hello():
    name,sur_name=map(lambda x: x.title(),input().split())
    print(f"Уважаемый, {name} {sur_name}! Вы верно выполнили это задание!")


say_hello()