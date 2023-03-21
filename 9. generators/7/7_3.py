#
num=dict(zip(('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'),range(1,8)))
lst=input().split()
res=sorted(lst,key=lambda x:num[x])
print(*res)
