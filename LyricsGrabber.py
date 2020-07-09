import re
import lyricsgenius
import pyperclip
import keyboard
import time
import applescript
#clientid
genius = lyricsgenius.Genius("_nJBLJrPt5bazD70r56qQw9YlC7nK7odl7OYsdJ0gfChihg6kjvFMHvwrIaAHJxT")
local_path='/Users/aaryamansmacbook/Library/Scripts/Send imessage.scpt'
minRegex = re.compile(r'(.*) - (.*)')
alist = [line for line in open('/Users/aaryamansmacbook/Desktop/mainsongs.txt')]
#Counter of songs done- (0,100) means it will do from index 0 up to song with index 99.
#The last state of the program was (0,100)
for x in range(2860,2870 ):
    mo = minRegex.search(alist[x])
    track=mo.group(1)
    singer=mo.group(2)
    #tryna fix timeout
    while True:
        try:
            song = genius.search_song(track, singer) #necessary line
            break
        except:
            pass           
    #end of timeout fix
    try:
        pyperclip.copy(song.lyrics)
    except AttributeError:
        pyperclip.copy('')


    finally:
        
#__init__(self, source=None, path=local_path)
#run(self, *args)

# 1. Run script:

        keyboard.send('command+h')
        

        keyboard.send('down')
    
        keyboard.send('tab')
        
        keyboard.send('tab')
        
        keyboard.send('enter')

        time.sleep(1)
        
        keyboard.send('down')

        time.sleep(1)

        print("The index of song is "+str(x)+'\n')
        
        
        
        
       

print('donezo')


 
