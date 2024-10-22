# Создаём кортеж immutable_var
immutable_var = (18, 'Артем', 34, 'Верно')
print(immutable_var)
# immutable_var[0] = 0
# выдаёт ошибку
mutable_list = ["городской", "Артем", 1, 2]
mutable_list[0] = "U"
mutable_list[1] = "А"
print(mutable_list)