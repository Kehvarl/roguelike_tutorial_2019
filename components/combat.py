class Combat:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def attack(self, target):
        results = []

        damage = self.power - target.combat.defense

        if damage > 0:
            results.append({'message': '{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(damage))})
            results.extend(target.combat.take_damage(damage))
        else:
            results.append({'message': '{0} attacks {1} to no effect'.format(self.owner.name.capitalize(), target.name)})

        return results

