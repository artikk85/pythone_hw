def my_func(x, y):
    result = 1
    if x <= 0 or y >= 0:
        for _ in range(abs(y)):
            result *= 1/x
        print(result)
    else:print('введите коректные данные!')
my_func(
    float(input('введите положительное число: ')),
    int(input('введите отрицательное число: '))
)
