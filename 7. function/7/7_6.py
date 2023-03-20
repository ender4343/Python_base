#

def get_path(n:int):
    if n<=1:
        return 1
    elif n==2:
        return 2
    return get_path(n-1)+get_path(n-2)
N=int(input())
print(get_path(N))