#На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел. Необходимо задать функцию с именем get_menu, которая преобразует эту строку в список из слов и возвращает этот список. Сигнатура функции, следующая:

def show_menu(func):
    def inner(*args):
        for i,v in enumerate(func(*args)):
            print(f'{i+1}. {v}')
    return inner
@show_menu
def get_menu(s:str):
    return s.split()
