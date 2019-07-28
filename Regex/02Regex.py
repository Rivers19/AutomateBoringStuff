"""
管理复杂的正则表达式
author@jiangchuan 20190718

向re.compile()传入变量re.VERBOSE 作为第二个参数; 从而可以添加#注释
"""

import re, pyperclip

# 电话号码正则表达式
phoneRegex  = re.compile(r'''(
    (\d{3}|\(\d{3}\))？          # area code
    (\s|-|\.)?                  # separator
    (\d{3})                     # first 3 digits
    (\s|-|\.)                   # separator
    (\d{4})                     # last 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# 电子邮箱正则表达式
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE)

# 剪贴板文本中找到匹配
text = str(pyperclip.paste())
matches = []                                                     # 所有的匹配保存在matches的列表变量中
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])       # phoneNum变量包含一个字符串，由匹配文本的分组1、3、5和8构成（这些分组分别是区号、前3个数字、后4个数字和分机号）
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
# 所有匹配连接成一个字符串，复制到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))                   # pyperclip.copy()函数只接收一个字符串值，而非字符串列表，故而在matches上使用了join()方法
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')