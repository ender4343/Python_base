#Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет, можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина третьей стороны всегда должна быть меньше суммы двух других). Если  проверка проходит, вернуть булево значение True, иначе - значение False.
def is_triangle(a,b,c):
    res=sorted([a,b,c])
    return res[2]<res[0]+res[1]