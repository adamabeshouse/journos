import curses
import curses.wrapper
import time

stdscr = curses.initscr() # initialize curses
curses.noecho() # don't automatically print typed characters to the screen
curses.cbreak() # react to keys instantly without requiring Enter to be pressed
stdscr.keypad(1) # make curses return special values like curses.KEY_LEFt

stdscr.addstr("5")
stdscr.refresh()
time.sleep(1)
stdscr.addstr("4")
stdscr.refresh()
time.sleep(1)
stdscr.addstr("3")
stdscr.refresh()
time.sleep(1)
stdscr.addstr("2")
stdscr.refresh()
time.sleep(1)
stdscr.addstr("1")
stdscr.refresh()
time.sleep(1)
stdscr.addstr("0")
stdscr.refresh()
curses.nocbreak(); stdscr.keypad(0); curses.echo() # close the application
curses.endwin() # return the terminal to its original operating mode
