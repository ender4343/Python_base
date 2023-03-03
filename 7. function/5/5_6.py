# (Для закрепления предыдущего материала). Вводится таблица целых чисел (см. пример ниже) размером N x N элементов (N определяется по входным данным). Эта таблица содержит нули, но кое-где - единицы. С помощью функции с именем verify, на вход которой передается двумерный список чисел, необходимо проверить, являются ли единицы изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.


def verify(lst):
    def is_isolate(lst,y,x):
        y_n=len(lst)
        x_n=len(lst[0])
        borders=((0,1),(1,1),(1,0))
        return any([(lst[y][x]+lst[y+i][x+j])>1 for i,j in borders if y+i<y_n and x+j<x_n])
    for y,v1 in enumerate(lst):
        for x,v2 in enumerate(v1):
            if is_isolate(lst,y,x):
                return False
        print(f"{round(y/len(lst)*100,2)}%")
    return True


print(verify(lst_in),lst_in.__sizeof__())