# LyricsGrabber
A python program that grabs lyrics from Genius and sets them to mp3 files. Note: All your music files must be in one common folder of you choice. You can even have folders of music within that main folder

How to use:
1. Open the LyricsGrabber python file in IDLE or any other editor of your choice. You simply have to change the pathname variable to path of the folder where all your music files are saved.

2. Sign up for a genius API and then click on generate ClientID. Enter this string in the LyricsGrabber program. There is a comment highlighting where to copy it.

3. If you have any songs which are by multiple artists, genius won't recognize them. There is a comment in the program that mentions artists delimiters. Change it to whatever character is in between the artists name. For example, if you had Asap Rocky/ Kendrick Lamar/ J.Cole, the delimiter would be a "/".

4. Run the program from IDLE. Don't worry about any errors as long as the program stil continues running. If there is an error and the program stops, bring it up in the issues page.

5. Wait until completion

Install the following dependencies:
1. lyricsgenius- https://pypi.org/project/lyricsgenius/
2. EyeD3- https://eyed3.readthedocs.io/en/latest/
