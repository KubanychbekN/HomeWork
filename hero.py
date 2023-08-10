class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name
    def double_health(self):
        self.health_points *= 2

    def info(self):
        print(f"Nickname: {self.nickname}\n"
              f"Superpower: {self.superpower}\n"
              f"Health: {self.health_points}")

    def length_catchphrase(self):
        return len(self.catchphrase)

hero = SuperHero("Tony Stark", "Iron Man", "genius intellect", 100, "I am Iron Man")

print("Hero's name:", hero.get_name())

hero.double_health()
print("Doubled health:", hero.health_points)

hero.info()

catchphrase_length = hero.length_catchphrase()
print("Length of catchphrase:", catchphrase_length)

print('-----------------')

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase,fly, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage
        self.fly = False

    def squaring_health(self):
        self.health_points **= 2
        self.fly = True

    def fly_phrase(self):
            return f"fly in the True_phrase"




airhero = AirHero("James Rhodes", "Iron Patriot", "iron man suit", 80, "I am America's protector", "Sky", 50)

airhero.info()
airhero.squaring_health()
print("Health points:", airhero.health_points)
print("Fly:", airhero.fly)
print(airhero.fly_phrase())

print('-----------------')

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase,fly, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage
        self.fly = True

    def squaring_health(self):
        self.health_points **= 2
        self.fly = True

    def fly_phrase(self):
            return f"fly in the True_phrase"





earthero= EarthHero("Steve Rogers", "Captain America", "Super Soldier", 200, "I am captain america", "Land", 100)

earthero.info()
earthero.squaring_health()
print("Health points:", earthero.health_points)
print("Fly:", earthero.fly)
print(earthero.fly_phrase())

print('-----------------')

class :
    people = "Monster"

    def gen_x(self):
        pass

    def crit(self,degree):
        return self.damage ** degree



