#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, argparse, os, re

parser = argparse.ArgumentParser(
    description="A simple bookmark manager for the command-line",
    epilog="")
exgroup = parser.add_mutually_exclusive_group()
exgroup.add_argument("-a", "--add", help="add a bookmark", metavar="title")
exgroup.add_argument("-c", "--copy", help="copy url to clipboard", metavar="id")
exgroup.add_argument("-d", "--delete", help="delete a bookmark by id", metavar="id")
exgroup.add_argument("-f", "--find", help="search for bookmarks containing substring", metavar="string")
exgroup.add_argument("-l", "--list", action="store_true", help="list all the bookmarks")
#exgroup.add_argument("-u", "--update", help="replace bookmark contents", metavar="id")
#exgroup.add_argument("-v", "--version", action="version", version="%(prog)s version 1.0")

args = parser.parse_args()

linksfilename = "links.txt"     #Store bookmarks in this file

#=====Class=====#
#
#class Bookmarks(list):
#
#    def __init__(self):
#        pass
#
#    def __str__(self):
#        pass
#
#=====Class=====#


def addLink(title, url):
    s = ""
    entry = [title, url]
    for elems in entry: s = s+elems+"\n"
    linksfile = open(linksfilename, "a")
    linksfile.write(s + "\n")
    linksfile.close()
    print "added bookmark: " + url
    return

def copyLink(b_id):
    all_the_links = linksParser()
    b_id = int(b_id)-1
    try:
        url = all_the_links[b_id][2]
    except:
        print "bookmark doesn't exist"
        return
    pyperclip.copy(url)
    print "copied to clipboard: " + url
    return

def delLink(b_id):
    all_the_links = linksParser()
    b_id = int(b_id)-1
    try:
        b_title = all_the_links[b_id][1]
    except:
        print "bookmark doesn't exist"
        return
    print(listLinks([all_the_links[b_id]])[0])
    choice = ""
    while (choice.lower() != "y") or (choice.lower() !="n"):
        choice = raw_input("\nreally delete this bookmark? y/n ")
        if choice.lower() == 'y':
            del all_the_links[b_id]
            string = ""
            for bookmarks in all_the_links:
                for c in [1, 2]:
                    string += bookmarks[c]+"\n"
                string += "\n"
            linksfile = open(linksfilename, "w")
            linksfile.write(string)
            linksfile.close()
            print "deleted \"" + b_title + "\""
            break
        elif choice.lower() == 'n':
            print("abort")
            break
    return

def findLink(search_string):
    all_the_links = linksParser()
    # Generate a list of bookmarks that match
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
    # Decide what to return
    if matches:
        return listLinks(matches)
    else:
        return None

def listLinks(all_the_links):
    linkstring = ""
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
    if total == 1:
        s = ""
    else:
        s = "s"
    totalsmessage = "%s bookmark" % total + s + " shown"
    return linkstring.strip("\n"), totalsmessage

def linksParser():
    """Prepares the bookmarks data for use by other functions"""
    linksfile = open(linksfilename)
    filecontents = linksfile.read()
    linksfile.close()
    # Generate a list of newline positions in the 'filecontents' variable
    newlines = []
    nlmarker = 0
    while nlmarker != -1:
        nlmarker = filecontents.find("\n", nlmarker+1)
        if nlmarker != -1:
            newlines.append(nlmarker)
    # Make lists out of title/url pairs, skipping newlines
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

if not os.path.exists(linksfilename):
    try:
        # Create the file if it doesn't exist
        linksfile = open(linksfilename, 'w')
    except IOError:
        print "error: couldn't create or access '" + linksfilename + "'"
        quit()
    finally:
        linksfile.close()

if args.add:
    turl = pyperclip.paste()
    if turl:
        addLink(args.add, turl)
    else:
        print "the clipboard is empty"
elif args.copy:
    if re.match("\d", args.copy): copyLink(args.copy)
    else: print "id must be a number"
elif args.delete:
    if re.match("\d", args.delete): delLink(args.delete)
    else: print "id must be a number"
elif args.find:
    listresults = findLink(args.find)
    if listresults:
        print listresults[0]
        print "\n" + listresults[1]
    else:
        print "no matches found"
elif args.list:
    listresults = listLinks(linksParser())
    if listresults[0]:
        print listresults[0]
        print "\n" + listresults[1]
    else:
        print "you don't have any bookmarks"
quit()
