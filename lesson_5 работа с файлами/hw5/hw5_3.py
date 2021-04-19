# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# with open('text_3.txt', 'r') as my_fail:
#     zp = []
#     surname = []
#     my_list = my_fail.read().split('\n')
#     for el in my_list:
#         el = el.split()
#         if int(el[1]) < 20000:
#             zp.append(el[0])
#             zp = ''.join(zp)
#             print(f'{zp} имеет оклад менее 20.000')
#         surname.append(el[0])
#     surname = (','.join(surname))
#     print(f'фамилии сотрудников: {surname}')


with open('text_3.txt', 'r') as my_fail:
    zp = []
    surname = []
    surnames = []
    my_list = my_fail.read().split('\n')
    for el in my_list:
        el = el.split()
        if int(el[1]) < 20000:
            surname.append(el[0])
            surname = ''.join(surname)
        zp.append(el[1])
        surnames.append(el[0])
    surnames = ', '.join(surnames)
print(f'{surname} имеет оклад меньше 20.000;\nсредний оклад сотрудника: '
      f'{sum(map(int, zp)) / len(zp)};\n'
      f'фамилии сотрудников: {surnames}')
