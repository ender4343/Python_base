#Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений, используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).
def get_rec_sum(lst:list[int],i=0,ans=0):
    ans+=lst[i]
    if i==len(lst)-1:
        return ans
    else:
        return get_rec_sum(lst,i+1,ans)


lst=list(map(int,input().split()))
print(get_rec_sum(lst))