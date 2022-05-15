#coding=utf-8
#! python3
# mcb.pyw - Save and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword>                            - Loads keyword to clipboard.
#           py.exe mcb.pyw <keyword>                              - Loads keyword to clipboard.
#           py.exe mcb.pyw list                                   - Loads all keywords to clipboard.
#           py.exe mcb.pyw delete <keyword>                       - Delete keyword from shelf.
#           py.exe mcb,pyw delete_all                             - Delete all keyword.
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
    elif sys.argv[1].lower() == 'change':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete_all':
        for keyword in mcbShelf.keys():
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
