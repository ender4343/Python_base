lst_in=['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
names = dict()

# формируем словарь
for pair in lst_in:
    key, value = pair.split()
    if key in names:
        names[key] += ', '
        names[key] += value
    else:
        names[key] = value
for key, value in names.items():
    print(f'{key}: {value}')