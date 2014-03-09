Clink
=====

Clink is a simple command-line tool for managing your bookmarks. The name stands for 'collect link'. At the moment, Clink simply dumps the contents of the clipboard (intended to be a URL) and a descriptive title to a 'links.txt' file.

The basic usage is:

`clink.py -a title`

This will append _title_ and the clipboard contents (a URL) to the links file. To view the links:

`clink.py -l`

I intend to implement tagging, viewing/sorting and searching functionality eventually. Since Clink uses the _Pyperclip_ module by Al Sweigart for clipboard handling, it has the potential to be cross-platform.
