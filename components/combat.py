class Combat:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        self.hp -= amount

    def attack(self, target):
        damage = self.power - target.combat.defense

        if damage > 0:
            target.combat.take_damage(damage)
            print('{} attacks {} for {} dmg'.format(self.owner.name, target.name, damage))
        else:
            print('{} fails to injure {}'.format(self.owner.name, target.name))

