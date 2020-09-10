user_list = list(input(' Введите список'))
i = 0
while i < len(user_list) - 1:
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i = i + 2

print(user_list)
