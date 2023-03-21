#Определите функцию с именем get_even_sum, которая принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) и вычисляет сумму только целых четных чисел, взятых из элементов итерируемого объекта. Результат возвращается функцией. Если целых чисел нет, то возвращается 0.
def get_even_sum(it):
    return sum(filter(lambda x: type(x)==int and x%2==0,it))
print(get_even_sum([*range(1,8),'asd','asd','asd']))