#Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n, которые кратны или 3 или 5. Результат (сумму) вывести на экран. Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.
res=sum([i for i in range(1,int(input()))if i%3==0 or i%5==0])
print(res)