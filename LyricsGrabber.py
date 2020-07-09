import re
import lyricsgenius
import pyperclip
import keyboard
import time
#clientid
numberofsongs=input("Enter number of songs")
genius = lyricsgenius.Genius("Enter clientID")
local_path='/Users/aaryamansmacbook/Library/Scripts/Send imessage.scpt'
minRegex = re.compile(r'(.*) - (.*)')
alist = [line for line in open('/Users/aaryamansmacbook/Desktop/mainsongs.txt')]
for x in range(0,numberofsongs ):
    mo = minRegex.search(alist[x])
    track=mo.group(1)
    singer=mo.group(2)
    while True:
        try:
            song = genius.search_song(track, singer) #necessary line
            break
        except:
            pass           
    try:
        pyperclip.copy(song.lyrics)
    except AttributeError:
        pyperclip.copy('')


    finally:

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
        
        
        
        
       

print('All done')


 
