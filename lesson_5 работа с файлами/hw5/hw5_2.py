# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('text_2.txt', 'a+') as my_fail:
    my_fail = my_fail.write(input('ведите текст: '))

my_fail = open('text_2.txt', 'r')
my_fail = (my_fail.readlines())
print(f'колличество строк в файле - {len(my_fail)}')

# в этом решении не получается перебрать слова в каждой строке
my_fail = open('text_2.txt', 'r')
while True:
    content = (my_fail.readline()).split()
    my_fail = (my_fail.readlines())
    for line in range(len(my_fail)):
        if len(content) != 0:
            print(f'в строке {line+1} содержиться {len(content)} слов')
    else:
        break

my_fail = open('text_2.txt', 'r')

# в этом решении не получается перебрать строки
while True:
    content = (my_fail.readline()).split()
    if len(content) != 0:
            print(f'в строке {line+1} содержиться {len(content)} слов')
    else:
        break

# with open('text_2.txt', 'r') as my_fail:
#     my_fail.read()
#     lines = 0
#     words = 0
#     for line in my_fail:
#         lines += line.count('\n')
#         words = len(line)- 1
#         print(f'в строке {line} содержиться {words} слов')











