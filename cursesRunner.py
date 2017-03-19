

def main(stdscr):
	stdscr = initscr()
	noecho()
	stdscr.addstr(0,0,'Hello World')
	stdscr.refresh()
	stdscr.getkey()

wrapper(main)