# def my_func(*args):
#     words = input('введите текст: ')
#     print(words.title())
# my_func()

def int_func(*args):
    latin = 'qwertyuiopasdfghjklzxcvbnm '
    while True:
        words = input('введите текст латинскими буквами: ')
        for el in words:
            if el not in latin:
                print('текст нужно ввести латинскими буквами!')
                break
        else:print(words.title())
int_func()