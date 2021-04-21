# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name}:'машина приехала'")

    def stop(self):
        print(f"{self.name}:'машина остановилась'")

    def turn(self, direction):
        print(f"{self.name}: машина повернула {'налево' if direction == 0 else 'направо'}")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}:'вы превысили скорость, скорость автомобиля: {self.speed}" )
        else:
            print(f'скорость автомобиля {self.name}: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}:'вы превысили скорость, скорость автомобиля: {self.speed}" )
        else:
            print(f'скорость автомобиля {self.name}: {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super.__init__(self, speed, color, name, is_police)
        #Car.__init__(self, speed, color, name, is_police)

kamaz = WorkCar(50, 'red', 'Kamaz', False)
print(kamaz.speed, kamaz.name, kamaz.color, kamaz.is_police)
print(kamaz.show_speed())

taxi = TownCar(60, 'yellow', 'Ford', False)
print(taxi.color, taxi.speed, taxi.name, taxi.is_police)
print(taxi.show_speed())