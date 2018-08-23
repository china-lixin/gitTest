#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import pyperclip
import requests
import sys
import webbrowser

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('https://mdb.baidu.com/' + address)
