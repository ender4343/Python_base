# Вводится список городов в одну строку через пробел. Если в этом списке присутствует город Москва, то удалить его. Вывести на экран результирующий список в виде строки с городами через пробел.
lst=list(input().split())
if "Москва" in lst:
    lst.remove("Москва")
print(*lst)