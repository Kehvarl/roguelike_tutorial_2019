import tcod as libtcod

def render_all(con, entities, screen_width, wcreen_height)
    for entity in entities:
        draw entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    libtcod.console_set_default_foregrount(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.chat, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    libtcod.console_put_char(cont, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

