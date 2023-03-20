#С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d. Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(d, ans:list=[]):
    for i in d:
        if type(i) is list:
            get_line_list(i,ans)
        else:
            ans.append(i)
    return ans
print(get_line_list(d))
