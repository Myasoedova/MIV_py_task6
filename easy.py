# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# class Cars:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self._is_police = False
#         self._model = name
#         print('***любая машина')
#         print('Скорость = {}, цвет = {}, name = {}'.format(speed,color,self._model))
#         if self._is_police:
#             print('полцейская')
#         else:
#             print('не полицейская')
#     def go(self):
#         print('Машина поехала')
#     def stop(self):
#         print('Машина остановилась')
#     def turn(self, dest):
#         print('Машина повернула', dest)
# class TownCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self._is_police = False
#         self._model = name
#         print('***Я только по городу')
#         print('Скорость = {}, цвет = {}, name = {}'.format(speed,color,self._model))
#         if self._is_police:
#             print('полцейская')
#         else:
#             print('не полицейская')
#     def town(self):
#         print('включаю городской режим движения')
#     def probki(self):
#         print('выбираем маршрут без пробок')
# class SportCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self._is_police = False
#         self._model = name
#         print('***sport car')
#         print('Скорость = {}, цвет = {}, name = {}'.format(speed,color,self._model))
#         if self._is_police:
#             print('полцейская')
#         else:
#             print('не полицейская')
#     def overdrive(self):
#         print('sport режим движения')
# class WorkCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self._is_police = False
#         self._model = name
#         print('***машина для работы')
#         print('Скорость = {}, цвет = {}, name = {}'.format(speed,color,self._model))
#         if self._is_police:
#             print('полцейская')
#         else:
#             print('не полицейская')
#     def worktype(self):
#         print('включаю маршрут для работы')
# class PoliceCar:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self._is_police = True
#         self._model = name
#         print('***полицейский авто')
#         print('Скорость = {}, цвет = {}, name = {}'.format(speed,color,self._model))
#         if self._is_police:
#             print('полцейская')
#         else:
#             print('не полицейская')
#     def police(self):
#         print('включаю режим полицейской машины')
# car1 = Cars('180','red','BMW')
# car2 = TownCar('60', 'white', 'Kia')
# car3 = SportCar('300', 'red', 'Ferrary')
# car4 = WorkCar('80', 'white','Audi')
# car5 = PoliceCar('100', 'white', 'Volksvagen')
# print(car1)
# print(car1.go())
# print(car1.turn('на улицу Красная площадь'))
# print(car2)
# print(car3)
# print(car3.overdrive())
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._model = name
        # self.type = 'любая машина'
        # print('***', self.type)
        print('***машина***')
        print('Скорость = {}, цвет = {}, name = {}'.format(speed,color,self._model))
        if self.is_police:
            print('полцейская')
        else:
            print('не полицейская')
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, dest):
        print('Машина повернула', dest)
class TownCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('*машина только по городу*')

    def town(self):
        print('включаю городской режим движения')
    def probki(self):
        print('выбираем маршрут без пробок')
class SportCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('*sport car*')
    def overdrive(self):
        print('sport режим движения')
class WorkCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('*машина для работы*')
    def worktype(self):
        print('включаю маршрут для работы')
class PoliceCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('* авто для полицейских*')
    def police(self):
        print('включаю режим полицейской машины')
car1 = Cars('180','red','BMW', 0)
car2 = TownCar('60', 'white', 'Kia', 0)
car3 = SportCar('300', 'red', 'Ferrary', 0)
car4 = WorkCar('80', 'white','Audi', 0)
car5 = PoliceCar('100', 'white', 'Volksvagen', 1)

print(car1)
print(car1.go())
print(car1.turn('на улицу Красная площадь'))
print(car2)
print(car3)
print(car3.overdrive())
print(car5.police())