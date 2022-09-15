class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range
 
    def hit(self, actor, target):
        if not target.is_alive():
            print('Враг уже повержен')
        else:
            t_x = target.get_coords()[0]
            t_y = target.get_coords()[1]
            a_x = actor.get_coords()[0]
            a_y = actor.get_coords()[1]
            if ((t_x - a_x) ** 2 + (t_y - a_y) ** 2) ** 0.5 > self.range:
                print(f'Враг слишком далеко до оружия {self.name}')
            else:
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.get_damage(self.damage)
 
    def __str__(self):
        return self.name
 
 
class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y, self.hp = pos_x, pos_y, hp
 
    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y
 
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False
 
    def get_damage(self, amount):
        self.hp -= amount
 
    def get_coords(self):
        return (self.pos_x, self.pos_y)
 
 
class BaseEnemy(BaseCharacter):

    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon
        
    def hit(self, target):
        if type(target) is MainHero:
            self.weapon.hit(target)
        else:
            print('Могу ударить только Главного героя')
 
    def __str__(self):
        return f'Враг на позиции {self.pos_x, self.pos_y} с оружием {self.weapon}'
 
 
class MainHero(BaseCharacter):

    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.weapon = None

    def hit(self, target):
        if self.weapon:
            if type(target) is BaseEnemy:
                self.weapon.hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')
 
    def add_weapon(self, weapon):
        if type(weapon) is Weapon:
            print(f'Подобрал {weapon}')
            self.weapons.append(weapon)
            if not self.weapon:
                self.weapon = weapon
        else:
            print('Это не оружие')
 
    def next_weapon(self):
        if not self.weapon:
            print('Я безоружен')
        elif len(self.weapons) == 1:
            print('У меня только одно оружие')
        else:
            self.weapon = self.weapons[(self.weapons.index(self.weapon) + 1) % len(self.weapons)]
            print(f'Сменил оружие на {self.weapon}')
 
    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')

weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)  