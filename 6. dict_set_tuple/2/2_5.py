things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
rev_t={things[i]:i for i in things}
srt_keys=sorted((rev_t.keys()),reverse=True)
N=int(input())*1000
to_get=[]
i=0
while True:
    t=srt_keys.pop(0)
    if N-t>=0:
        to_get+=[t]
        N-=t
    if len(srt_keys)==0:break
for i in to_get:
    print(rev_t[i],end=' ')


    