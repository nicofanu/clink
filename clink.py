#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, argparse

parser = argparse.ArgumentParser(
    description="A simple bookmark manager for the command-line",
    epilog="And that's all folks!")

exgroup = parser.add_mutually_exclusive_group()
exgroup.add_argument("-a", "--add", help="add a bookmark", metavar="item")
exgroup.add_argument("-l", "--list", action="store_true", help="list all the bookmarks")
#exgroup.add_argument("-v", "--version", action="version", version="%(prog)s version 1.0")
args = parser.parse_args()

linksfilename = "links.txt"

def addLink(title, url):
    linksfile = open(linksfilename, "a")
    linksfile.write(title+"\n"+url+("\n"*2))
    linksfile.close()
    print("Added bookmark: "+url)

def listLink():
    all_the_links = linksParser()
    print all_the_links

def linksParser():
    linksfile = open(linksfilename)
    filecontents = linksfile.read().strip('\n')
    linksfile.close()
    return filecontents

if args.add:
    turl = pyperclip.paste()
    if turl:
        addLink(args.add, turl)
    else:
        print("The clipboard is empty.")
elif args.list:
    listLink()

quit()
