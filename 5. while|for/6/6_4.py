
lst_in=[[1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0], 
        [0, 1, 0, 1, 0], 
        [0, 0, 0, 0, 0]]
y_x_borders=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
res=True
for y,row in enumerate(lst_in):
    for x ,cell in enumerate(row):
        for i,j in y_x_borders:
            if y+i>4 or x+j>4 or 0>y+i or 0>x+j:
                continue
            if cell+lst_in[y+i][x+j]>1:
                res=False
print('ДА'if res else'НЕТ')
                
