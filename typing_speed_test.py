import curses


stdscr = curses.initscr()
answer = curses.newwin(15,15, 12,0)
#curses.start_color

#curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.clear()
word = "Hello World!"
stdscr.addstr(10,0, word)
stdscr.refresh()

correct = []
"""
x = 0

for let in word:
    a = answer.getch(12,x)
    x += 1
    stdscr.move(12,x)
    stdscr.refresh()
    
    #if a == ord("b"):
        #stdscr.addstr(10,0, word, curses.A_STANDOUT)
        #stdscr.refresh()
    
    if a == ord(" "):
        answer.clear()
        x = 0
        answer.refresh()
"""

x = 0
y = len(word)
z = y
q = 0
while z != 0:
    a = answer.getch(12,x)
    x += 1
    if a == ord(word[q]):
        q += 1
        z -= 1
        if a == ord(" "):
            answer.clear()
            x = 0
            answer.refresh()





curses.nocbreak()
stdscr.keypad(False)
#curses.echo()