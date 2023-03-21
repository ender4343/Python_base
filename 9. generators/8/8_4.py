#Определите функцию с именем get_list_dig, которая возвращает список только из числовых значений переданной ей коллекции (список или кортеж).
def get_list_dig(it):
    return list(filter(lambda x: type(x) in (int,float) ,it))