#
lst_in=['8 11 -5', '3 4 10', '-1 -2 3', '4 5 6']
lst2D=[list(map(int,x.split()))for x in lst_in]
print(lst2D)