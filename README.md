# LyricsGrabber
A Mac-Only UI automation program that grabs lyrics from Genius and sets them in an iTunes friendly format. Note: Your music files need to be on iTunes

How to use:
1. You need to install a few scripts from Doug's applescripts including:
https://dougscripts.com/itunes/scripts/ss.php?sp=cliptomultilyrics and 
https://dougscripts.com/itunes/scripts/ss.php?sp=explaylistastext

2. Go into the songs menu. Use the applescript that exports playlist info to clipboard and choose the option that says song and artist only. Save this to a text file

3. Run the clean-up text program to ensure that the text file is formatted properly. You can edit the file path information based on where you saved your text file

4. https://dougscripts.com/itunes/itinfo/shortcutkeys.php. Follow this guide to assign command+H to run the clipboard to multi-track lyrics script.

5. Sign up for a genius API and copy the client ID to the LyricsGrabber program

6. Run the LyricsGrabber program, and immediately click away and select the first song in the "Songs" menu on iTunes. Ensure that itunes remains in the foreground and you don't click away

7. Wait until completion

Dependencies:
1.lyricsgenius- https://pypi.org/project/lyricsgenius/
2.python keyboard- https://pypi.org/project/keyboard/
3.pyperclip- https://pypi.org/project/pyperclip/
