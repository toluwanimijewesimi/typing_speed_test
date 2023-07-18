import curses

stdscr = curses.initscr()
curses.start_color()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.clear()
curses.init_pair(1, 1, 2)
stdscr.addstr (10,0, "Hello World!", curses. color_pair(1))
stdscr.refresh()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()