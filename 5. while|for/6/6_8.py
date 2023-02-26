moneys=[2**x for x in range(6,-1,-1)]
coast=int(input())
lst=[]
for i in moneys:
    while coast-i>=0:
        coast-=i
        lst.append(i)
print(lst)