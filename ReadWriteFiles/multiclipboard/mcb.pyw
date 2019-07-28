"""
多重剪贴板
author@jiangchuan20190719

.pyw意味着你python运行该程序时，不会显示终端窗口

该程序将利用一个关键字保存每段剪贴板文本
mcb.pyw %*

eg. 当运行py mcb.pyw save spam 剪贴板中当前的内容就用关键字spam保存，运行py mcb.pyw save spam 这段文本稍后会重新加载到剪贴板
若忘记了都有哪些关键字，可以运行 py mcb.pyw list 将所欲关键字的列表复制到剪贴板

程序需要做的事情：
- 针对要检查的关键字，提供命令行参数
- 若参数是save，将剪贴板内容保存到关键字
- 若参数是list，将所有关键字拷贝到剪贴板
- 否则，将关键字对应的文本拷贝到剪贴板

代码需要做的事情：
- 从sys.argv读取命令行参数
- 读写剪贴板
- 保存并加载shelf文件

"""
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