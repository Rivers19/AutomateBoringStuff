#! python
# mcb.pyw - Save and loads pieces of text to clipboard
# Usage: py.exe mcb.pyw save <keyword> -Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> -Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys                               # 读取命令行参数需要sys模块、粘贴需要pyperclip模块

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':    # 如果第一个命令行参数是字符串save，
    mcbShelf[sys.argv[2]] = pyperclip.paste()               # 第二个命令行参数就是保存剪贴板当前内容的关键字。关键字将用作mcbShelf中的键，值就是当前剪贴板上的内容
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':                        # 如果只有一个命令行参数，首先检查是否是list
        pyperclip.copy(str(list(mcbShelf.keys())))          # 是则表示shelf键的列表的字符串将被拷贝到剪贴板。用户可将该列表拷贝到一打开的文本编辑器进行查看
    elif sys.argv[1] in mcbShelf:                           # 否则，假定该命令行参数是一个关键字，若其是shelf中的一个键，可以将对应的值加载至剪贴板
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()