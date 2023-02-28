
lst_in=[[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9], 
        [5, 4, 3]]

lst=[[ lst_in[x][y] for x in range(len(lst_in))] for y in range(len(lst_in[0]))] 
for i in lst:
    print(*i)