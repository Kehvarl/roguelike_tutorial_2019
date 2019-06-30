import tcod as libtcod


def handle_keys(key):
    # Movement Keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0,-1)}
    if key.vk == libtcod.KEY_DOWN:
        return {'move': (0,1)}
    if key.vk == libtcod.KEY_LEFT:
        return {'move': (-1,0)}
    if key.vk == libtcod.KEY_RIGHT:
        return {'move': (1,0)}
        
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}
