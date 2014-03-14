#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, argparse

parser = argparse.ArgumentParser(
    description="A simple bookmark manager for the command-line",
    epilog="And that's all folks!")

exgroup = parser.add_mutually_exclusive_group()
exgroup.add_argument("-a", "--add", help="add a bookmark", metavar="item")
exgroup.add_argument("-d", "--delete", help="delete a bookmark by id", metavar="id")
exgroup.add_argument("-l", "--list", action="store_true", help="list all the bookmarks")
exgroup.add_argument("-f", "--find", help="search for bookmarks containing substring", metavar="string")
#exgroup.add_argument("-v", "--version", action="version", version="%(prog)s version 1.0")
args = parser.parse_args()

linksfilename = "links.txt"

def addLink(title, url):
    s = ""
    entry = [title, url]
    for elems in entry: s = s+elems+"\n"
    linksfile = open(linksfilename, "a")
    linksfile.write(s + "\n")
    linksfile.close()
    print("added bookmark: "+url)
    return

def delLink(b_id):
    all_the_links = linksParser()
    b_id = int(b_id)-1
    b_title = all_the_links[b_id][1]
    print(listLinks([all_the_links[b_id]])[0])
    print("\nreally delete this bookmark? y/n ")
    del all_the_links[b_id]
    string = ""
    for bookmarks in all_the_links:
        for c in [1, 2]:
            string += bookmarks[c]+"\n"
        string += "\n"
    linksfile = open(linksfilename, "w")
    linksfile.write(string)
    linksfile.close()
    print("\""+b_title+"\" deleted")
    return

def findLink(search_string):
    all_the_links = linksParser()
    ## Generate a list of bookmarks that match
    matches = []
    n = 0
    for a in range(0, len(all_the_links)):
        flag = 0
        for b in [1, 2]:
            string = all_the_links[a][b].lower()
            x = string.find(search_string.lower())
            if x >= 0 and flag == 0:
                matches.append(all_the_links[a])
                flag = 1
                b_id = a + 1
                temps = all_the_links[a]
                temps.extend([b_id])
    ## Decide what to return
    if matches:
        return listLinks(matches)
    else:
        return "no matches found"

def listLinks(all_the_links):
    linkstring = ""
    linksshown = ""
    for bookmarks in all_the_links:
        linkstring += "%s: " % bookmarks[0]
        for c in [1, 2]:
            if c == 2:
                space = "   "
            else:
                space = ""
            linkstring += space+bookmarks[c]+"\n"    
        linkstring += "\n"
    total = len(all_the_links)
    if total > 1:
        s = "s"
    else:
        s = ""
    totalsmessage = "%s bookmark" % total + s + " shown"
    return linkstring.strip("\n"), totalsmessage

def linksParser():
    """Prepares the bookmarks data for use by other functions"""
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
    ## Make lists out of title/url pairs, skipping newlines
    bookmarks = []
    templist  = []
    x         = 0
    c         = 0
    b_id      = 1
    for y in newlines:
        if c == 2:
            bookmarks.append(templist)
            templist = []
            c = 0
        if filecontents[x:y] != "":
            if not templist:
                templist.append(b_id)
                b_id += 1
            templist.append(filecontents[x:y])
            c += 1
        x = y + 1
    return bookmarks

if args.add:
    turl = pyperclip.paste()
    if turl:
        addLink(args.add, turl)
    else:
        print("the clipboard is empty")
elif args.delete:
    delLink(args.delete)
elif args.find:
    listresults = findLink(args.find)
    print(listresults[0])
    print("\n"+listresults[1])
elif args.list:
    listresults = listLinks(linksParser())
    print(listresults[0])
    print("\n"+listresults[1])

quit()
