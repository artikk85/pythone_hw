def my_func(*args):
    words = (my_func())
    print(words.title())

my_func(
    input('введите слова через пробел: ')
)