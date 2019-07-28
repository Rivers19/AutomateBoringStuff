#!/usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:             # 若参数个数大于
    
    # Get addrese from clipboard
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
    
webbrowser.open('https://map.baidu.com/search/' + address)