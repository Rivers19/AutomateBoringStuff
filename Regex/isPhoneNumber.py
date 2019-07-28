
#%%
"""
定义一个在字符串中查找电话号码的函数
author@jiangchuan 20190717
"""

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('414-555-4532 is a phone number :')
print(isPhoneNumber('414-555-4532'))
print('hello hello is a phone number:')
print(isPhoneNumber('hello hello'))


#%%
"""
在for循环的每一次迭代中，取自message的一段新的12个字符被赋给变量chunk。
将chunk传递给isPhoneNumber()，看是否符合电话号码的模式，如果符合则打印这段文字。
继续遍历message，最终chunk中的12个字符会是一个电话号码。该循环遍历了整个字符串，测试了每一段12个字符，打印了所有满足isPhoneNumber()的chunk

使用正则表达式查找电话号码的类似程序和本程序一样，运行也不会超过1秒钟，但是正则表达式编写更快捷
"""
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my offfice.'
for i in range(len(message)):
    chunk = message[i: i+12]
    if isPhoneNumber(chunk):
        print('Phone number found:' + chunk)
print('Done')


#%%



