#естовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам). На вход программы поступают различные URL-адреса. Если адрес пришел впервые, то на экране отобразить строку (без кавычек):
#"HTML-страница для адреса <URL-адрес>"
#Если адрес приходит повторно, то следует взять строку "HTML-страница для адреса <URL-адрес>" из словаря и вывести на экран сообщение (без кавычек):
#"Взято из кэша: HTML-страница для адреса <URL-адрес>"
#Сообщения выводить каждое с новой строки.
#P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
lst_in=['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm', 'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii', 'ustanovka-i-poryadok-raboty-pycharm']
d={}
for i in lst_in:
    if i not in d:
        d[i]="HTML-страница для адреса"
        print(f'{d[i]} {i}')
    else:
        print(f'Взято из кэша: {d[i]} {i}')