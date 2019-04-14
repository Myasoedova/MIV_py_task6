# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name
        print('Данные игрока: имя = {}, health = {}, damage = {}, armor = {}'.format(name, health, damage, armor))

class Player(Person):

    # Функция для подсчета урона
    def _calculate_damage(self, damage, armor):
        return damage // armor

    # Функция атаки, принимает на вход 2 структуры
    def attack(self, who_attack, who_defend):
        damage = Player._calculate_damage(self, who_attack.damage, who_defend.armor)
        who_defend.health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, damage,
                                                                        who_defend.health))

class Enemy(Person):
    # Функция для подсчета урона
    def _calculate_damage(self, damage, armor):
        return damage // armor

    # Функция атаки, принимает на вход 2 структуры
    def attack(self, who_attack, who_defend):
        damage = Enemy._calculate_damage(self, who_attack.damage, who_defend.armor)
        who_defend.health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, damage,
                                                                        who_defend.health))

# Функция старта игры, передадим аргументом игрока, который играл последним .
def start_game(gamer):
    # Запоминаем кто последний атаковал
    last_attacker = gamer
    while player_name.health > 0 and enemy_name.health > 0:
        if last_attacker == gamer and player_name.name == gamer.name:
            enemy_name.attack(enemy_name, player_name)
            last_attacker = enemy_name
        else:
            player_name.attack(player_name, enemy_name)
            last_attacker = player_name

    if player_name.health > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')

# Создаем наши структуры данных
player_name = Player(input('введите имя игрока'), 100, 50, 0.9)
enemy_name = Enemy(input('введите имя игрока'), 100, 50, 0.7)

start_game(player_name)


# player_name.attack(player_name,enemy_name)