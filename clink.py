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
exgroup.add_argument("-f", "--find", help="search for bookmarks containing string", metavar="string")
#exgroup.add_argument("-v", "--version", action="version", version="%(prog)s version 1.0")
args = parser.parse_args()

linksfilename = "links.txt"

def addLink(title, url):
    linksfile = open(linksfilename, "a")
    s = ""
    entry = [title, url]
    for elems in entry: s = s+elems+"\n"
    linksfile.write(s + "\n")
    linksfile.close()
    print("Added bookmark: "+url)

def findLink(search_string):
    all_the_links = linksParser()
    ## Generate a list of bookmarks with matches
    matches = []
    for a in range(0, len(all_the_links)):
        flag = 0
        for b in [0, 1]:
            string = all_the_links[a][b].lower()
            x = string.find(search_string.lower())
            if x >= 0 and flag == 0:
                matches.append(all_the_links[a])
                flag = 1
    ## Some code to craft the results string 'found'
    return #found

def listLink():
    all_the_links = linksParser()
    s = ""
    n = 1
    for bookmarks in all_the_links:
        s += "%s: " % n
        for elems in bookmarks:
            s += elems+"\n"
        s += "\n"
        n += 1
    return s.strip("\n")

def linksParser():
    linksfile = open(linksfilename)
    filecontents = linksfile.read()
    linksfile.close()
    ## Generate a list of newline positions in the 'filecontents' variable
    newlines = []
    nlmarker = 0
    while nlmarker != -1:
        nlmarker = filecontents.find("\n", nlmarker+1)
        if nlmarker != -1:
            newlines.append(nlmarker)
    ## Make lists out of title/url pairs
    bookmarks = []
    templist  = []
    x         = 0
    c         = 0
    for y in newlines:
        if c == 2:
            bookmarks.append(templist)
            templist = []
            c = 0
        if filecontents[x:y] != "":
            templist.append(filecontents[x:y])
            c += 1
        x = y + 1
    return bookmarks

if args.add:
    turl = pyperclip.paste()
    if turl:
        addLink(args.add, turl)
    else:
        print("The clipboard is empty.")
elif args.find:
    print(findLink(args.find))
elif args.list:
    print(listLink())

quit()
