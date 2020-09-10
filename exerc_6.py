struct = []
init = 'да'
num = 1
while init == 'да':

    name = input('Введите название товара')
    price = input('Введите цену товара')
    qu = input('Введите количество товара')
    unity = input('Введите единицу измерения')
    struct1 = [(num, {'Название': name, 'Цена': price, 'Количество': qu, 'Ед. изм.': unity})]
    struct.extend(struct1)
    num = num + 1
    for i in struct:
        print(i)
    ini = input('Если желаете добавить товар введите да')
    init = ini.lower()
names = []
prises = []
qus = []
units = []
for i in struct:
    names.append(i[1].get('Название'))
    prises.append(i[1].get('Цена'))
    qus.append(i[1].get('Количество'))
    units.append(i[1].get('Ед. изм.'))
analysis = {'Название': names, 'Цена': prises, 'Количество': qus, 'Ед. изм.': units}
init1 = input('Если желаете вывести аналитику товаров введите да')
if init1.lower() == 'да':
    print(analysis)
init3 = input('Для вывода характеристик товара введите цифры: название -1; цена-2; количество- 3; единиц измерения-4 ')
if init3 == "1":
    print(analysis.get('Название'))
if init3 == "2":
    print(analysis.get('Цена'))
if init3 == "3":
    print(analysis.get('Количество'))
if init3 == "4":
    print(analysis.get('Ед. изм.'))
