top = [9, 6, 4, 2]
print(top)
init = 'да'
while init == 'да':
    init = 'нет'
    num = int(input('Введите натуральтное число'))
    if num in top:
        n = top.count(num)
        m = top.index(num)
        top.insert(m + n, num)
    else:
        m = 0
        for i in top:
            if num < i:
                m = m + 1
        top.insert(m, num)
    print(top)
    init = input('Желаете продолжить заполнение рейтинга? Введите да для продолжения')
    init = init.lower()
