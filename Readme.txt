Python script to automatically open up imdb link of the movie whose folder/file is given as
parameter to the python script via "Send-to" in Windows.

How to check which python you're using.
-Open command prompt --> type python --> Hit enter
-If You've set the python path in in system environment variables it'll show the python version and python IDLE
-else it'll show "python is not recognized as an internal windows"

How to switch between Python 2.x and Python 3.x
-Download Python 2.x and 3.x from "https://www.python.org/downloads/"
-Install the python 1.x and 3.x in different directories.
-Now if you want to use python2 by default, set the path of Python2 in system environment variables, do the same if you want to use Python3
-If you're using Python2 already, just download and install Python3 in different directory, set path if you want to use it.

Note: If you want to use Python3.x also with Python2.x. Just install the python3.x in a different directory than Python2 and set the path in system environment variables.

Usage (imdb-lookup.py):
[Use 'imdb-lookup.py' for Python2 and 'imdb-lookup-Python3.py' for Python3]

Copy imdb-lookup.py file to C:\
Copy the IMDB-lookup.cmd file to your sendto folder in Windows (can be accessed by typing shell:sendto in addressbar or Win+R)
Right click on a movie folder(of a single movie) and click Sendto->IMDB-lookup.py

Your default browser opens up with IMDB page of the movie.

Usage (imdb-folder.py):
[Works only for Python2]

Copy imdb-folder.py file to C:\
Copy the IMDB-folder.cmd file to your sendto folder in Windows (can be accessed by typing shell:sendto in addressbar)
Right click on a movies folder(consisting of multiple movie folders inside of it) and click SendTo->IMDB-folder.py

Voila! Excel spreadsheet opens up with all details fetched from Imdb like genre,rating,actors,awards etc
All the extra information in the file/folder name like DVDrip,aXXo etc are removed in the script so as to search the database.

Usage(imdb-rating-folder.Py)
[Use 'imdb-rating-folder-Python2.py' for Python2 and 'imdb-rating-folder-Python3.py' for Python3]

Copy imdb-rating-folder-Python2.py file to C:\
Copy imdb-rating-folder-Python2.cmd in the movies folder in which movie folders are there.
Double click on imdb-rating-folder-Python2.cmd, it'll execute imdb-rating-folder-Python2.py and your movies will be renamed with 
moviename with IMDB ratings.
ex. The.legend.of.tarzan.2016.1080p.xSpark --> The legend of tarzan - IMDB 6.3
Note:
-Don't keep any files in the folder which is not a movie like .exe etc
-Script may fail if movie name contains any ripper name which script doesn't handle
-Please report if any issue is there.

For Ubuntu :
Place open_in_browser.sh and send_folde.sh in ~/.gnome2/nautilus-scripts. U can see them in Scripts -> when u right click.
Place imdb-lookup and imdb-folder.py on desktop.


More explanation can be found here:http://qr.ae/GxOcx
a How-to video can be found here : http://youtu.be/JANNcimQGyk

