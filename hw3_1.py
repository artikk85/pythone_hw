def my_func(a, b):
    if b !=0:
        print(a / b)
    else:print('на 0 делить нельзя!')

my_func(
    int(input('введите число а: ')),
    int(input('введите число b: '))
)
