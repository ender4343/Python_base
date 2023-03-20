#Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника), которая выводит сообщение (без кавычек)
def get_info(width:int,height:int):
    res=(width+height)*2
    print(f"Периметр прямоугольника, равен {res}")
arr=list(map(int,input().split()))

get_info(*arr)

