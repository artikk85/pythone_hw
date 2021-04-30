# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class Division_by_Zero(Exception):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def division_by_zero(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return ('делить на 0 нельзя')

print(Division_by_Zero.division_by_zero(50, 0))
