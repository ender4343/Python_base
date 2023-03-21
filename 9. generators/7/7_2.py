
lst_in=['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']
lst=list(map(lambda x: tuple(x.split("=")),lst_in))
lst.sort(key=lambda x: int(x[-1]),reverse=True)
for i in lst:
    print(i[0],end=" ")