Python script to automatically open up imdb link of the movie whose folder/file is given as
parameter to the python script via "Send-to" in Windows.

Does NOT work with Python 3.x

Usage (imdb-lookup.py):

Copy imdb-lookup.py file to C:\
Copy the IMDB-lookup.cmd file to your sendto folder in Windows (can be accessed by typing shell:sendto in addressbar)
Right click on a movie folder(of a single movie) and click Sendto->IMDB-lookup.py

Your default browser opens up with IMDB page of the movie.

Usage (imdb-folder.py):

Copy imdb-folder.py file to C:\
Copy the IMDB-folder.cmd file to your sendto folder in Windows (can be accessed by typing shell:sendto in addressbar)
Right click on a movies folder(consisting of multiple movie folders inside of it) and click SendTo->IMDB-folder.py

Voila! Excel spreadsheet opens up with all details fetched from Imdb like genre,rating,actors,awards etc


All the extra information in the file/folder name like DVDrip,aXXo etc are removed in the script so as to search the database.

For Ubuntu :
Place open_in_browser.sh and send_folde.sh in ~/.gnome2/nautilus-scripts. U can see them in Scripts -> when u right click.
Place imdb-lookup and imdb-folder.py on desktop.


More explanation can be found here:http://qr.ae/GxOcx
a How-to video can be found here : http://youtu.be/JANNcimQGyk





