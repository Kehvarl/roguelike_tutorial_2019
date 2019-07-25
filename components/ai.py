import tcod as libtcod
from game_messages import Message


class BasicMonster:
    def __init__(self):
        self.owner = None

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            
            if monster.distance_to(target) >= 2:
                monster.move_astar(target, entities, game_map)
            elif target.combat.hp > 0:
                attack_results = monster.combat.attack(target)
                results.extend(attack_results)

        return results


class DeadMonster:
    corpse_labels = ['corpse', 'skeleton', 'bones', 'skull']

    def __init__(self):
        self.owner = None

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        monster = self.owner
        if not libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if not hasattr(monster, 'deadtime'):
                monster.deadtime = 5

            monster.deadtime -= 1

            if monster.deadtime == 0:
                results.append({'message': Message('Something changes', libtcod.white)})
                self.decay(monster)
                monster.deadtime = 5

        return results

    def decay(self, monster):
        index = DeadMonster.corpse_labels.index(monster.label)
        if index + 1 < len(DeadMonster.corpse_labels):
            monster.label = DeadMonster.corpse_labels[index + 1]
        else:
            monster.fade = True


class ActiveDeadMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        return results
