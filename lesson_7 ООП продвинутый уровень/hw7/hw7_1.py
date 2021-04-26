# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return ('\n'.join(map(str, self.list)))

    def __add__(self, other):
        my_new_matrix = []
        for i in range(len(self.list)):
            my_new_matrix.append([])
            for j in range(len(self.list[0])):
                my_new_matrix[i].append(self.list[i][j] + other.list[i][j])
        return '\n'.join(map(str, my_new_matrix))



my_matrix1 = Matrix([[1, 1, 2, 1], [2, 5, 6, 7], [3, 4, 5, 8]])
my_matrix2 = Matrix([[1, 4, 2, 8], [3, 5, 7, 9], [5, 5, 5, 8]])
print(my_matrix1, '\n')
print(my_matrix2, '\n')
print(my_matrix1 + my_matrix2)