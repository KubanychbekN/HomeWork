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