#Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел. Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа дополнительно ставить символ диеза '#'. Реализовать эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a,b,c=map(int,input())
dies=(0,3)
ff=lambda x: "#"+m[x] if x in dies else x
print(ff(a),ff(b),ff(c))