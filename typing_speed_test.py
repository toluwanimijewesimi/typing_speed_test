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
#def current_word(setence):
    #hello

'''
for letter in sentence:
    if letter == " ":
        words.append(letter)
    else:
        hold = letter
        check = letter
        while check != " ":
            check += 1
            if check == " ":
                letter = check
        words.append(sentence[hold, check])
'''
li_sentence = []
typed = []

for lett in sentence:
    li_sentence.append(ord(lett))

cursor = 0
sentence_len = len(sentence)
sentence_index = 0
while sentence_len != 0:
    type = answer.getch(12,cursor)
    cursor += 1
    typed.append(type)
    for errorz in typed:
        if errorz == 127:
            typed.remove(errorz)
    if type == ord(sentence[sentence_index]):
        if typed == li_sentence[:sentence_index + 1]:
            sentence_index += 1
            sentence_len -= 1
            if type == ord(" "):
                answer.clear()
                cursor = 0
                answer.refresh()
    if type == 127:
        answer.delch(12, cursor)
        answer.delch(12, cursor - 1)
        answer.delch(12, cursor - 2)
        cursor -= 2
        typed.pop()
        answer.refresh()
'''
#incorporate into main code
index_ = 0
checker = 1
while index_ != len(typed) + 1:
    for let in typed:
        if let == letters[index_]:
            index_ += 1
        else:
            checker = -1
    if checker == 1:
        print("True")
            
'''
 


curses.nocbreak()
stdscr.keypad(False)
#curses.echo()