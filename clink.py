#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, os, sys

nargs = len(sys.argv)    # Will be useful later when I figure out argument parsing
linksfile = open('links.txt', 'a')

def printUsage():
    print("Usage is: %s <title>" % os.path.basename(sys.argv[0]))

def addLink():
    if (nargs>1):
        title = sys.argv[1]
        url = pyperclip.paste()    
        if (url):
            linksfile.write(title+"\n"+url+("\n"*2))
        else:
            print("The clipboard is empty.")
    else:
         printUsage()
         
addLink()
linksfile.close()
