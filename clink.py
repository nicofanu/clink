#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, argparse

parser = argparse.ArgumentParser(
    description="A simple bookmark manager for the command-line",
    epilog="And that's all folks!")

exgroup = parser.add_mutually_exclusive_group()
exgroup.add_argument("-a", "--add", help="Add a bookmark", metavar="item")
exgroup.add_argument("-l", "--list", action="store_true", help="List all the bookmarks")
args = parser.parse_args()

def addLink(title, url):
        linksfile = open('links.txt', 'a')
        linksfile.write(title+"\n"+url+("\n"*2))
        linksfile.close()
        print("Added bookmark: "+url)

def listLink():
    linksfile = open('links.txt')
    filecontents = linksfile.read()
    print filecontents
    linksfile.close()
         
if args.add:
    turl = pyperclip.paste()
    if turl:
        addLink(args.add, turl)
    else:
        print("The clipboard is empty.")
elif args.list:
    listLink()

quit()
