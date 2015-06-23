Clink
=====

Clink is a small Python script to quickly store and recall URLs from the terminal. I wrote it because I just wanted a way to manage bookmarks without needing to open my browser or have an internet connection. It's quick because of the way it works with the OS clipboard (via [pyperclip](http://github.com/asweigart/pyperclip)) to eliminate some typing effort. It should work on Windows, Mac and Linux.

Basic Usage
-----------
Here's how I would use it. In a normal browsing session, I will come across an interesting website or article that I want to keep for later. I select the URL and press **ctrl+c**. Then I switch to a terminal and enter `clink -a "title"`. 

    user@system:~$ clink -a "Interesting URL shortener"  
    added bookmark 119: https://is.gd/



Later on I'll search for the bookmark with a keyword such as "interesting".

    user@system:~$ clink -l interesting  
    119: Interesting URL shortener  
         https://is.gd/  

    1 bookmark shown


Now I can copy the URL back into the clipboard. 

    user@system:~$ clink -c 119  
    copied to clipboard: https://is.gd/  


If I later want to delete it from the list:

    user@system:~$ clink -d 119
    119: Interesting URL shortener
         https://is.gd/

    really delete this bookmark? y/n y
    deleted 'Interesting URL shortener'

Notes:

* On Linux, you need to have:
    * either the _xclip_ or _xsel_ programs installed and
    * and either the _gtk_ or _PyQt4_ modules
* URLs are logged in a text file, "links.txt" in the same location as the script
* You can change the location of the text file by editing the variable `links_txt_name`
* If you don't specify a title, the current date will be used
