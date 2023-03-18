def get_biggest_city(*citys):
    lst=[len(x)for x in citys]
    max_ind=lst.index(max(lst))
    return citys[max_ind]
print(get_biggest_city('Питер','Москва','Самара','Воронеж'))