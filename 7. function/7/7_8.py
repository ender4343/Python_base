#Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
lst_in=list(map(int,input().split()))
def merge_lst(a:list,b:list):
    l_a=len(a)
    l_b=len(b)
    i=j=0
    res=[]
    while l_a>i and l_b>j:
        if a[i]<=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    res+=a[i:]+b[j:]
    return res

def split_and_merge(a):
    n=len(a)//2
    a1=a[:n]
    a2=a[n:]

    if len(a1)>1:
        a1=split_and_merge(a1)
    if len(a2)>1:
        a2=split_and_merge(a2)
    
    return merge_lst(a1,a2)
print(split_and_merge(lst_in))