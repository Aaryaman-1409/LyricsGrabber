import os
import eyed3
import lyricsgenius
genius = lyricsgenius.Genius("XDm__srBeFR1EZqt6B_ZkMxfZnOtTcrGOl7UbfCZCU4g07C98SPQ4RyswEbqvPjL")
# add genius client ID

pathname='/Users/aaryamansmacbook/Desktop/Deemix Downloads'
#Change folder location if needed

import os
for root, dirs, files in os.walk(pathname, topdown=True):
    for name in files:
        filename=os.path.join(root, name)
        if ".jpg" in filename or ".png" in filename:
            continue
        else:
            audiofile = eyed3.load(filename)
            track = audiofile.tag.title
            singer = audiofile.tag.artist
            if "/" in singer:
                #Change slash to whatever delimiter is between the artists name
                words= singer.split('/')
                singer = words[0]
            #tryna fix timeout
            while True:
                try:
                    song = genius.search_song(track, singer) #necessary line
                    break
                except:
                    pass
            #end of timeout fix
            try:
                audiofile.tag.lyrics.set(song.lyrics)
                
            except AttributeError:
                print('No lyrics found')
                audiofile.tag.lyrics.set('')

            finally:
                audiofile.tag.save(version=eyed3.id3.ID3_DEFAULT_VERSION,encoding='utf-8')

print('all done')
                
                
            
            

    

