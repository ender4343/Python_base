#Составить программу поиска всех трехзначных чисел, которые при делении на 47 дают в остатке 43 и кратны 3. Вывести найденные числа в строчку через пробел. Программу реализовать при помощи цикла while.
i=100
lst=[]
while i!=999:
    if i%47==43 and i%3==0:
        lst.append(i)
    i+=1
print(*lst)