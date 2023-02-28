#
st1=set(map(int,input().split()))
st2=set(map(int,input().split()))
res=st1-st2
print(*sorted(res))