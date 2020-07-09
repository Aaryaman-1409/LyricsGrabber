import re
import lyricsgenius
minRegex = re.compile(r'(.*) - (.*)')
semiRegex=re.compile('[^;]+')
alist = [line for line in open('/Users/aaryamansmacbook/Desktop/mainsongs copy.txt')]
copyfile=open('/Users/aaryamansmacbook/Desktop/mainsongs.txt', 'w')
for x in alist:
    mo = minRegex.search(x)
    track=mo.group(1)
    singer=mo.group(2)
    so=semiRegex.search(singer)
    singer=(so.group())
    copyfile.write(track+' - '+singer+'\n')
copyfile.close()
    





print('done')


