# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def get_cloth(self):
        pass

    def __add__(self, other):
        return self.get_cloth + other.get_cloth

class Cloak(Clothes):
    @property
    def get_cloth(self):
        return round(self.param / 6.5 + 0.5)

class Costume(Clothes):
    @property
    def get_cloth(self):
        return round((self.param * 2 + 0.3) / 100)

my_cloak = Cloak(52)
my_costume = Costume(185)

print(my_cloak + my_costume)
