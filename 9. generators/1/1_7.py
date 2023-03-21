#
f=lambda x: 0.5 * pow(x, 2) - 2.0
a,b=map(int,input().split())
gen=(round(f(i/100),2) for i in range(a*100,100*(b+1)))
for i in range(20):
    print(next(gen),end=" ")