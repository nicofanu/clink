#! /usr/bin/env python

# Clink - the CLI URL collector
# Author: Nicholay Nascimento

import pyperclip, argparse, os, time

parser = argparse.ArgumentParser(
    description="A simple bookmark manager for the command-line",
    epilog="")
exgroup = parser.add_mutually_exclusive_group()
exgroup.add_argument("-a", "--add", help="add a bookmark", metavar="title", nargs='?',
    const=time.strftime("%Y-%m-%d"))
exgroup.add_argument("-c", "--copy", help="copy url to clipboard", metavar="id")
exgroup.add_argument("-d", "--delete", help="delete a bookmark by id", metavar="id")
exgroup.add_argument("-l", "--list", const=True,
    help="list all bookmarks or just those containing TERM", metavar="term", nargs='?')

args = parser.parse_args()

links_txt_name = "links.txt"                  #Store bookmarks in this file

def addLink(title, url):
    """Saves a new bookmark"""
    bookmarks = linksParser()
    bookmark_id = len(bookmarks)
    new_entry = {'id'    : bookmark_id,
                 'title' : title,
                 'url'   : url
                 }
    bookmarks.append(new_entry)
    writeLinks(bookmarks)
    print "added bookmark %s: " % (new_entry['id'] + 1) + url
    return

def writeLinks(bookmarks):
    """Handles the actual writing of the bookmarks to the text file"""
    nl                   = "\n"
    string               = ""
    last = len(bookmarks)
    for i in range(last):
        if i + 1 == last: nl = ""
        string += bookmarks[i]['title'] + "\n"
        string += bookmarks[i]['url'] + nl
        string += nl
    links_txt = open(links_txt_name, 'w')
    links_txt.write(string)
    links_txt.close()
    return

def copyLink(bookmark_id):
    """Copies a bookmark URL to the clipboard"""
    bookmarks = linksParser()
    bookmark_id = int(bookmark_id)-1
    try: url = bookmarks[bookmark_id]['url']
    except IndexError:
        print "bookmark doesn't exist"
        quit()
    pyperclip.copy(url)
    print "copied to clipboard: " + url
    return

def delLink(bookmark_id):
    """Deletes a bookmark and saves the changes to file"""
    bookmarks            = linksParser()
    bookmark_id          = int(bookmark_id)-1
    choice               = ""
    try: title           = bookmarks[bookmark_id]['title']
    except IndexError:
        print "bookmark doesn't exist"
        quit()
    listLinks([bookmarks[bookmark_id]])
    while choice.lower() != ("y" or "n"):
        try: choice = raw_input("really delete this bookmark? y/n ")
        except KeyboardInterrupt:
            print "\nabort"
            break
        if choice.lower() == 'y':
            del bookmarks[bookmark_id]
            writeLinks(bookmarks)
            print "deleted '%s'" % title
            break
        elif choice.lower() == 'n':
            print("abort")
            break
    return

def findLink(search_string):
    bookmarks = linksParser()
    if search_string == True:                 #List all bookmarks by default if
        return listLinks(bookmarks)           #no search string specified
    else:
        matches              = []
        result               = -1
        for i in range(len(bookmarks)):
            already_found_in_vals = False     #Reset flag
            for key in bookmarks[i]:
                if not key == 'id':           #Skip searching the id
                    string = bookmarks[i][key].lower()
                    result = string.find(search_string.lower())
                if result >= 0 and not already_found_in_vals:
                    matches.append(bookmarks[i])
                    already_found_in_vals = True
        if matches:
            return listLinks(matches)
        else:
            return "no matches found"

def listLinks(bookmarks):
    """Neatly prints the bookmarks and returns their total amount"""
    if bookmarks:
        pad              = " "
        digits           = len(str(bookmarks[-1]['id']))
        fix_padding      = (digits+2) * pad   #Spacing before URLs, always fixed
        total_bookmarks  = len(bookmarks)
        for i in range(total_bookmarks):
            x = (digits - len(str(bookmarks[i]['id'])))
            if x != 0:
                dyn_padding = x * pad         #Spacing before IDs, changes to 
            else:                             #keep text aligned
                dyn_padding = ""
            print "%s%s: %s" % (dyn_padding, bookmarks[i]['id'], bookmarks[i]['title'])
            print "%s%s\n" % (fix_padding, bookmarks[i]['url'])
        if total_bookmarks > 1: s = "s"       #This one's for the Grammar Nazis
        else: s = ""
        return "%s bookmark%s shown" % (total_bookmarks, s)
    else:
        return "you have no bookmarks"

def linksParser():
    """Prepares bookmarks data for use by other functions"""
    raw_links            = []
    bookmarks            = []
    tempdict             = {}
    count                = 1
    bookmark_id          = 1
    links_txt = open(links_txt_name)
    templist = links_txt.read().splitlines()
    links_txt.close()
    for i in range(len(templist)):
        if templist[i]:                       #Grow a new list, skipping
            raw_links.append(templist[i])     #those pesky empty strings
    for i in range(len(raw_links)):
        if count == 1:
            tempdict['id'] = bookmark_id
            tempdict['title'] = raw_links[i]
            bookmark_id += 1
        else:
            tempdict['url'] = raw_links[i]
            bookmarks.append(tempdict)
            tempdict = {}
            count = 0
        count += 1
    return bookmarks

if not os.path.exists(links_txt_name):
    try:
        links_txt = open(links_txt_name, 'w') #Create the file if it doesn't exist
    except IOError:
        print "error: couldn't create or access '%s'" % links_txt_name
        quit()
    finally:
        links_txt.close()

if args.add:
    turl = pyperclip.paste()
    if turl:        addLink(args.add, turl)
    else:           print "the clipboard is empty"
elif args.copy:
    if args.copy.isdigit(): copyLink(args.copy)
    else:           print "not a valid id"
elif args.delete:
    if args.delete.isdigit(): delLink(args.delete)
    else:           print "not a valid id"
elif args.list:
    print findLink(args.list)
else:
    parser.print_help()
