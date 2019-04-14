# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.
class Factory:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self._type = 'Игрушка'
        print('name = {}, color = {}, type = {}'.format(name, color, self._type))
    def buyer(self):
        print('закупка сырья')
    def shit(self):
        print('пошив')
    def paint(self):
        print('окраска')
class Animal(Factory):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Animals'
        print('Тип :', self._type)
class Multi(Factory):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Мультиперсонаж'
        print('Тип: ' , self._type)
toy1 = Factory('pig','red')
toy2 = Animal('bear','yellow')
toy3 = Multi('Mouse','Black')
print(toy1, toy2, toy3)
print(toy2.paint())
print(toy3.buyer(),'для персонажа типа', toy3.name)
# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Mouse(Multi):
    def gets(self):
        print(self.name, ' ИЗ Multi Mouses')
class Volf(Animal):
    def gets(self):
        print(self.name, ' ИЗ Animal Volf')
mik = Mouse('Mouse1','red')
nil = Volf('Volf1','gray')
def my_get(type):
    type.gets()

my_get(mik)
my_get(nil)