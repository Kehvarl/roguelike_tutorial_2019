import tcod as libtcod

def render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    draw_map(con, game_map, fov_map, fov_recompute, colors)

    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_map(con, game_map, fov_map, fov_recompute, colors):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        color = colors.get('light_wall')
                    else:
                        color = colors.get('light_ground')
                else:
                    if wall:
                        color = colors.get('dark_wall')
                    else:
                        color = colors.get('dark_ground')
                draw_tile(con, x, y, color)

def draw_tile(con, x, y, color):
    libtcod.console_set_char_background(con, x, y, color, libtcod.BKGND_SET)


def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

