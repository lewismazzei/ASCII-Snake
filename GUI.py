import curses
height = 500
width = 500
begin_y = (curses.LINES / 2) - 250
begin_x = (curses.COLS / 2) - 250
win = curses.newwin(height, width, begin_y, begin_x)

curses.cbreak()
win.keypad(True)




