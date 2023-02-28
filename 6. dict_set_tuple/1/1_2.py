
s=['5=отлично', '4=хорошо', '3=удовлетворительно']
d={}
for i in s:
    x,y=i.split('=')
    d[int(x)]=y
print(d)