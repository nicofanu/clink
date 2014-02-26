# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip

file = open('links.txt', 'a')

def addLink():
    title = "Test"
    url = pyperclip.paste()

    print "URL is: "+url
    if (url):
        file.write(title+"\n"+url+"\n")
    else:
        print "The clipboard is empty."

addLink()
