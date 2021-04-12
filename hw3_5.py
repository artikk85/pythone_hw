def sum_nam():
    s = 0
    while True:
        list_num = input('введите числа через пробел, для выхода нажмите q: ').split()
        for i in list_num:
            if i == 'q':
                return s
            else: s += int(i)
        print(s)

sum_nam()