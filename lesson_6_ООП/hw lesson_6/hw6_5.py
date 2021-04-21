# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        # Stationery.draw(self)
        print(f'{self.title}-синяя ручка')

class Pencil(Stationery):
    def draw(self):
        # Stationery.draw(self)
        print(f'{self.title}-автоматический карандаш')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title}-нестираемый маркер')

pilot_pen = Pen('Pilot_h1')
pilot_pen.draw()

pilot_pencil = Pencil('Pilot_hp2')
pilot_pencil.draw()

pilot_handle = Handle('Pilot_hxw3')
pilot_handle.draw()
