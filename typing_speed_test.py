import curses
import time
from random import choice

stdscr = curses.initscr()
wpm_win = curses.newwin(3, 90, 0, 0)
display = curses.newwin(6, 90, 3, 0)
answer = curses.newwin(3, 90, 8, 0)
curses.start_color()
curses.use_default_colors()

wpm_win.refresh()

#curses.noecho()
curses.cbreak()
stdscr.keypad(True)

#initializes color pairs
curses.init_pair(1, 2, -1)
curses.init_pair(2, 7, 1)

start = True
play = False
stdscr.clear()
wpm_win.addstr(1, 1, 'Welcome to the Typing Speed Test \n Press space to start the test, or the ">" key at any time to quit.')
wpm_win.refresh()
wait = 0
while wait != ord (" ") and wait != (">"):
    wait = answer.getch(1, 1)
    if wait == ord(" "):
        play = True
        wpm_win.clear()
    elif wait == ord(">"):
        wpm_win.clear()
        wpm_win.addstr(1, 0, "Thanks for playing!")
        wpm_win.refresh()
        break


while play == True:
    with open("sentences.txt") as file:
        sentences = file.readlines()
        sentence = choice(sentences)
        sentence = sentence.strip()
        #sentence = "Filler"

    #word = "Hello World!"

    li_sentence = [] #empty list for all the letters in the sentece, in order
    typed = [] #empty list for all the letters the user has tpyed
    correct = []

    #appends all letters in sentence to the appropriate list
    for lett in sentence:
        li_sentence.append(ord(lett))

    #print out sentence list one letter at a time
    y = 1
    x = 1

    for a in li_sentence:
        a = chr(a)
        display.addstr(y,x, a)
        if a == " ":
            if x > 70 and x < 80:
                x = 0
                y += 1
        display.refresh()
        x += 1

    wpm_win.addstr(1, 1, "WMP: 0")
    wpm_win.addstr(1, 11, f"Accuracy: 0%")
    wpm = 0
    accuracy = 0

    wpm_win.refresh()

    cursor = 1 #starting point for cursor
    sentence_len = len(sentence)
    sentence_index = 0 #tracks what letter the user needs to type currently

    typed_count = 0
    correct_count = 0

    start_time = time.time()


    #allows user to enter letters until they have typed all the letters
    while True:
        try:
            type = answer.getch(1,cursor)
            if type == ord(">"):
                break
        except:
            break
        cursor += 1 #incriments cursor to display next letter next to the previous letter
        typed.append(type)
        #dont add deletes to the coun
        if type != 127:
            typed_count += 1
        #removes all the backspace inputs that are automatically added to the tyed list
        for errorz in typed:
            if errorz == 127:
                typed.remove(errorz)
        #checks if entered letter matches expected letter
        if type == ord(sentence[sentence_index]):
            #makes sure the complete sentence is acurate and not jsut the current letter by comparing the list of typed letters and expected letters
            if typed == li_sentence[:sentence_index + 1]:
                sentence_index += 1 #moves expected letter to next letter
                sentence_len -= 1 #reduces letters needed to be typed sentece is complted
                correct.append(type)
                correct_count += 1
                #clears line if previous word was spelt correclty and funtions as the space in the sentence
                if type == ord(" "):
                    answer.clear()
                    cursor = 1
                    answer.refresh()
        else:
            curses.beep()
        #allows backspace to be used in terminal and removes the backspaced letter from letters in list of typed letters
        if type == 127:
            if cursor == 1 or cursor == 2:
                answer.clear()
                answer.refresh()
                cursor = 1
            else:
                answer.delch(1, cursor)
                answer.delch(1, cursor - 1)
                answer.delch(1, cursor - 2)
                cursor -= 2
                if correct == typed:
                    typed.pop()
                    correct.pop()
                    sentence_index -= 1
                    sentence_len += 1
                else:
                    typed.pop()
                answer.refresh()
        #highlight text based on wether the input is correct or not and add moving cursor
        
        #display.clear()

        

        #print correct as green
        #display.clear()
        y1 = 1
        x1 = 1
    
        for l in sentence[:len(correct)]:
            display.chgat(y1, x1, 1, curses.color_pair(1))
            if l == " ":
                if x1 > 70 and x1 < 80:
                    x1 = 0
                    y1 += 1
            display.refresh()
            x1 += 1
        
        #print wrong as red
        y2 = y1
        x2 = x1
        for l in sentence[len(correct):len(typed)]:
                display.chgat(y2, x2, 1, curses.color_pair(2))
                if l == " ":
                    if x2 > 70 and x2 < 70:
                        x2 = 0
                        y2 += 1
                display.refresh()
                x2 += 1

        #print cursor
        y3 = y2
        x3 = x2
        #for l in sentence[len(typed)]:
        display.chgat(y3, x3, 1, curses.A_REVERSE)
        if l == " ":
            if x3 > 70 and x3 < 70:
                x3 = 0
                y3 += 1
        display.refresh()
        x3 += 1

        #clear deleted cursor
        y4 = y3
        x4 = x3
        #for l in sentence[len(typed)]:
        display.chgat(y4, x4, 1, curses.color_pair(0))
        if l == " ":
            if x4 > 70 and x4 < 70:
                x4 = 0
                y4 += 1
        display.refresh()
        x4 += 1

        #calculate wpm
        end_time = time.time()

        elapsed_time = end_time - start_time
        sec_to_min = elapsed_time/60
        wpm = (len(correct)/5)/sec_to_min
        wpm = round(wpm)

        #calculate accuracy
        accuracy = (correct_count/typed_count) * 100
        accuracy = round(accuracy)

        #show wpm
        wpm_win.clear()
        wpm_win.addstr(1, 1, f"WMP: {wpm}")
        wpm_win.addstr(1, 11, f"Accuracy: {accuracy}%")
        wpm_win.refresh()

        if len(correct) == len(sentence):
            answer.clear()
            break


    wpm_win.clear()
    wpm_win.addstr(1, 1, f"WMP: {wpm}")
    wpm_win.addstr(1, 11, f"Accuracy: {accuracy}%")
    answer.addstr(2, 1, 'Great job, enter space to play again or the ">" key to quit.')
    wpm_win.refresh()
    wait = 0
    wait = answer.getch(1, 1)
    if wait == ord(" "):
        start = True
        wpm_win.clear()
        answer.clear()
        display.clear()
    else:
        start == False
        wpm_win.clear()
        wpm_win.addstr(1, 0, "Thanks for playing!")
        wpm_win.refresh()
        break

    



    

    #display.addstr(y, x, sentence[:len(correct)], curses.color_pair(1))
    #display.addstr(1, len(correct) + 1, senence[len(correct):len(typed)], curses.color_pair(2))
    #display.addstr(1, len(typed) + 1, sentence[len(typed)], curses.A_REVERSE)
    #display.addstr(1, len(typed) + 2, sentence[len(typed) + 1:])


curses.nocbreak()
stdscr.keypad(False)
#curses.echo()