# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text_5.txt', 'w+')as my_fail:
    my_fail.write(' '.join([str(randint(1, 100)) for i in range(100)]))
    my_fail.seek(0)
    print(sum(map(int, my_fail.read().split())))