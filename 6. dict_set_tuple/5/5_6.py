#Вводятся два списка городов каждый с новой строки (в строке названия через пробел), которые объехал Сергей в 1-й и 2-й годы своего путешествия по России. Требуется определить, включал ли его маршрут во 2-й год все города 1-го года путешествия? Если это так, то вывести ДА, иначе - НЕТ.
st1=set(input().lower().split())
st2=set(input().lower().split())
print('ДА' if st2>st1 else 'НЕТ')