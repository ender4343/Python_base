def get_data_fig(*args,**kwargs):
    tccw=('type', 'color', 'closed', 'width')
    temp=tuple()
    for i in tccw:
        if i in kwargs:
            temp+=(kwargs[i],)
    return(sum(args),*temp)