# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as my_file:
    for el in  my_file:
        el = el.split()
        new_file.append(rus[el[0]] + '-' + el[0])
print('; '.join(new_file))

with open('text_4new.txt', 'w') as my_file:
    my_file = my_file.write(str(new_file))
print(new_file)