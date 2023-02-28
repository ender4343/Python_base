
lst_in=['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!', 'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю', 'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']
st=set([x.split(': ',1)[0][:-1] for x in lst_in])
print(len(st))