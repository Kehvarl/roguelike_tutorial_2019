import tcod as libtcod


def main():
    screen_width = 80
    screen_height = 50

    player_x = 25
    player_y = 40

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

    key = libtcod.key()
    mouse = libtcod.mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush()



if __name__ == "__main__":
    main()
