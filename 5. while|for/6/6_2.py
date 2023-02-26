#Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ дефиса (-). Следует учесть, что может быть несколько подряд идущих пробелов. Результат преобразования вывести на экран в виде строк из URL-адресов.
import sys

lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
for i,j in enumerate(lst_in):
    while '  'in lst_in[i]:
        lst_in[i]=lst_in[i].replace('  ',' ')
    lst_in[i]=lst_in[i].replace(' ','-')
print(*lst_in,sep='\n')