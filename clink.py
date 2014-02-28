#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, os, sys

nargs = len(sys.argv)    # Will be useful later when I figure out argument parsing

def printUsage():
    print("Usage is: %s <title>" % os.path.basename(sys.argv[0]))

def addLink():
    if (nargs>1):
        title = sys.argv[1]
        url = pyperclip.paste()    
        if (url):
            linksfile = open('links.txt', 'a')
            linksfile.write(title+"\n"+url+("\n"*2))
            linksfile.close()
        else:
            print("The clipboard is empty.")
    else:
         printUsage()

def viewLink():
    linksfile = open('links.txt')
    filecontents = linksfile.read()
    print filecontents
    linksfile.close()
         
addLink()
viewLink()
quit()
