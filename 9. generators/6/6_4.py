
lst_in=['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
d={int(j.split(":")[1]):j.split(":")[0] for j in lst_in}
min_values=sorted(d)[:3]
for i in min_values:
    print(d[i],end=" ")