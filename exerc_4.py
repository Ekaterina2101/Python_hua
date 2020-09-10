user_str = input('введите строку')
new_str = user_str.split()
for ind, el in enumerate(new_str, 1):
    if len(el) > 10:
        el = el[:10]
    print(ind, el)
