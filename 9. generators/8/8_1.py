#Определите функцию с именем get_add, которая складывает или два числа или две строки (но не число со строкой) и возвращает полученный результат. Если сложение не может быть выполнено, то функция возвращает значение None. Сигнатура функции должна быть, следующей:
def get_add(a,b):
    if {type(a),type(b)} in ({str,},{int,},{float,},{int,float}):
        return a+b