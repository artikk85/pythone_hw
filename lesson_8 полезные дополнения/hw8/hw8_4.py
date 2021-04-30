# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Store_office_equipment:
    def __init__(self, name, model, price, quantity, *args):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = quantity
        self.central_store = []
        # self.my_unit = {}

    def __str__(self):
        return f'наименование: {self.name}-{self.model}; цена: {self.price}; колличество: {self.quantity}'

    def to_central_store(self):
        # while True:
            try:
                get_name = input('введите наименование: ')
                get_model = input('введите модель: ')
                get_price = int(input('введите цену: '))
                get_quantity = int(input('введите колличество: '))
                unit_characteristic = {'название': get_name, 'модель': get_model, 'цена за единицу': get_price,
                          'колличество': get_quantity}
                self.central_store.append(unit_characteristic)
                # self.my_unit.update(unit_characteristic)
                # self.central_store.append(self.my_unit)
                print(f'на склад принят товар: {unit_characteristic}')
            except:
                print('ошибка ввода информации! цена должна быть указана цифрами')

            print('для продолжения нажмите ENTER, для выхода нажмите Q ')
            q = input()
            if q == 'q' or q =='Q':
                return f'прием товара закончен, сейчас на центральном складе числяться: \n {self.central_store} \n'
            else:
               return Store_office_equipment.to_central_store(self)

    def to_shop_store(self):
        # try:
            get_name_to_shop_store = input('введите название или модель для перемещения в магазин: ')
            for el in self.central_store:
                unit = ''.join([value for value in el.values() if value == get_name_to_shop_store])
                if unit in el.values():
                    self.central_store.remove(el)
                    return f'товар: {unit} перемещен на склад магазина. \nна центральном складе: {self.central_store}'

        # except:
        #     print('нужно указать тавар для перемещения на склад магазина латинскими буквами,\n для продолжения нажмите '
        #           'ENTER, для выхода нажмите Q')
        #     q = input()
        #     if q == 'q' or q == 'Q':
        #         return f'выход'
        #     else:
        #         return Store_office_equipment.to_shop_store(self)


class Printer(Store_office_equipment):
    def to_print(self):
        return f'печатает'

class Scaner(Store_office_equipment):
    def to_scan(self):
        return f'сканирует'

class Xerox(Store_office_equipment):
    def to_xer(self):
        return f'копирует'


unit_1 = Printer('Canon', 'ZV8', 20000, 5)
unit_2 = Scaner('Sony', 'A6', 15000, 2)
unit_3 = Xerox('Xerox', '200-S', 10000, 8)


print(unit_1)
print(unit_2)
print(unit_3)
print(unit_1.to_central_store())
print(unit_1.to_shop_store())


