#Объявите функцию, которая принимает список, находит максимальное, минимальное и сумму значений этого списка и выводит результат в виде строки (без кавычек):
def get_info(arr):
    Min,Max,Sum=min(arr),max(arr),sum(arr)
    print(f"Min = {Min}, max = {Max}, sum = {Sum}")
ar=list(map(int,input().split()))
get_info(ar)