import os
import eyed3
import lyricsgenius
genius = lyricsgenius.Genius("add genius client ID here")
# add genius client ID

pathname='Copy music folder pathname here'
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
            #fixing timeout error
            while True:
                try:
                    song = genius.search_song(track, singer)
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

print('All files completed')
                
                
            
            

    

