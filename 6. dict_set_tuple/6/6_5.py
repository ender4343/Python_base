#Авторы с названиями могут повторяться. Необходимо, используя генераторы, сформировать словарь с именем d вида:
#{'автор 1': {'название 1', 'название 2', ..., 'название M'}, ..., 'автор K': {'название 1', 'название 2', ..., 'название S'}}
#lst_in = list(map(str.strip, open(0).readlines())); d = {}
#for key_value in lst_in:
#    key, value = key_value.split(': '); d.setdefault(key, set()).add(value)