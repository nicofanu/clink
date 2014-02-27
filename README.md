Clink
=====

Clink is a CLI tool written in Python for simple URL-keeping using plaintext files. The name stands for 'collect link'. At the moment, Clink simply dumps the contents of the clipboard and a supplied descriptive title to a 'links.txt' file in the current directory. So in other words, it's not ready for practical use yet. I intend to implement tagging, viewing/sorting and searching functionality eventually. Since Clink uses the _Pyperclip_ module by Al Sweigart for clipboard handling, it has the potential to be cross-platform.

The basic usage (while URL is in clipboard) is:

`clink.py <title>`
