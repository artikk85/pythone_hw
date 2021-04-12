def my_func(a, b, c):
    max_sum = [a, b, c]
    max_sum.sort(reverse=True)
    print(max_sum[0] + max_sum[1])

my_func(
    int(input('a=')),
    int(input('b=')),
    int(input('c=')),
        )