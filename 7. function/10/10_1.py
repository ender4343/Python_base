#спользуя замыкания функций, определите вложенную функцию, которая бы увеличивала значение переданного параметра на 5 и возвращала бы вычисленный результат. При этом внешняя функция должна иметь следующую сигнатуру:
def counter_add(numb):
    def add_numb():
        nonlocal numb
        return numb+5
    return add_numb
k = int(input())
cnt=counter_add(k)
print(cnt())