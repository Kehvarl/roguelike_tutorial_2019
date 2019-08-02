import tcod as libtcod


def handle_keys(key):
    key_char = chr(key.c)

    # Movement Keys
    if key.vk == libtcod.KEY_UP or key_char == 'w':
        return {'move': (0,-1)}
    if key.vk == libtcod.KEY_DOWN or key_char == 's':
        return {'move': (0,1)}
    if key.vk == libtcod.KEY_LEFT or key_char == 'a':
        return {'move': (-1,0)}
    if key.vk == libtcod.KEY_RIGHT or key_char == 'd':
        return {'move': (1,0)}

    if key_char == 'g':
        return {'pickup': True}
    
    if key_char == 'u':
        return {'move': (-1,-1)}
    if key_char == 'o':
        return {'move': (1,-1)}
    if key_char == 'j':
        return {'move': (-1,1)}
    if key_char == 'l':
        return {'move': (1,1)}

    
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}
