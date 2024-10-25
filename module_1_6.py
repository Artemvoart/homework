my_dict = {'Age': 2004, 'Lena': 89688664051}
print(my_dict)
print(my_dict.get("Lena"))
print(my_dict.get("Artem"))
my_dict.update({'Name': str('Alex'), 'Karl': 89158654051})
s = my_dict.pop('Name')
print(s)
print(my_dict)

# Создаём множества
my_set = {3, 2, 1, 6, "Yppe", 6, 2, 1, True}
print(my_set)
print(my_set.add("Josef"))
print(my_set.add("Mira"))
print(my_set.discard(2))
print(my_set)
