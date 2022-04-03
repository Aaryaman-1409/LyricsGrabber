# LyricsGrabber
A python program that grabs lyrics from Genius and sets them to mp3 files. Note: All your music files must be in one common folder of you choice. You can even have folders of music within that main folder

How to use:
1. Change the pathname variable to path of the folder where all your music files are saved.

2. Sign up for a genius API and then click on generate ClientID. Enter this string in the LyricsGrabber program.

3. If you have any songs which are by multiple artists, genius won't recognize them. There is a comment in the program that mentions artists delimiters. Change it to whatever character is in between the artists name. For example, if you had Asap Rocky/ Kendrick Lamar/ J.Cole, the delimiter would be a "/".

Install the following dependencies:
1. lyricsgenius- https://pypi.org/project/lyricsgenius/
2. EyeD3- https://eyed3.readthedocs.io/en/latest/
