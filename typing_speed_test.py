import curses

stdscr = curses.initscr()
answer = curses.newwin(15,15, 12,0)
#curses.start_color

#curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.clear()
sentence = "The quick brown fox..."
#word = "Hello World!"
stdscr.addstr(10,0, sentence)
stdscr.refresh()

li_sentence = [] #empty list for all the letters in the sentece, in order
typed = [] #empty list for all the letters the user has tpyed

#appends all letters in sentence to the appropriate list
for lett in sentence:
    li_sentence.append(ord(lett))

cursor = 0 #starting point for cursor
sentence_len = len(sentence)
sentence_index = 0 #tracks what letter the user needs to type currently

#allows user to enter letters until they have typed all the letters
while sentence_len != 0:
    type = answer.getch(12,cursor)
    cursor += 1 #incriments cursor to display next letter next to the previous letter
    typed.append(type)
    #removes all the backspace inputs that are automatically added to the tyed list
    for errorz in typed:
        if errorz == 127:
            typed.remove(errorz)
    #checks if entered letter matches expeted letter
    if type == ord(sentence[sentence_index]):
        #makes sure the complete sence is acurate and not jsut the current letter by comparing the list of typed letters and expected letters
        if typed == li_sentence[:sentence_index + 1]:
            sentence_index += 1 #moves expected letter to next letter
            sentence_len -= 1 #reduces letters needed to be typed sentece is complted
            #clears line if previous word was spelt correclty and funtions as the space in the sentence
            if type == ord(" "):
                answer.clear()
                cursor = 0
                answer.refresh()
    #allows backspace to be used in terminal and removes the backspaced letter from letters in list of typed letters
    if type == 127:
        answer.delch(12, cursor)
        answer.delch(12, cursor - 1)
        answer.delch(12, cursor - 2)
        cursor -= 2
        typed.pop()
        answer.refresh()

curses.nocbreak()
stdscr.keypad(False)
#curses.echo()