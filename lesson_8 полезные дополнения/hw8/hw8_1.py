# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def in_num(cls, day_month_year):
        date = [i for i in day_month_year.split('-')]
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return day, month, year
                else:
                    return ('неверные входные данные - год')
            else:
                return ('неверные входные данные - месяц')
        else:
            return ('неверные входные данные - день')


print(Date.in_num('24-04-2021'))
print(Date.valid(12, 5, 2025))

