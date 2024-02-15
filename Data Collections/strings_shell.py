Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = "Ram Sharma"
name = 'Ram Sharma'
len(name)
10
type(name)
<class 'str'>
name[0]
'R'
name[6]
'a'
name[20]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    name[20]
IndexError: string index out of range
name
'Ram Sharma'
name[-1]
'a'
text = "Hello World"
text[4]
'o'
text[0:4]
'Hell'
text[5:10]
' Worl'
text[5:11]
' World'
text[:5]
'Hello'
text[5:]
' World'
text[:]
'Hello World'
text[0:11]
'Hello World'
text[0:11:1]
'Hello World'
text[0:11:2]
'HloWrd'
text[10:0]
''
text[10:0:-1]
'dlroW olle'

text[10::-1]
'dlroW olleH'
text[::-1]
'dlroW olleH'
text
'Hello World'
text[0] = "X"
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    text[0] = "X"
TypeError: 'str' object does not support item assignment
del text[0]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text = "Hello how are you..??"
text.lower()
'hello how are you..??'
text.upper()
'HELLO HOW ARE YOU..??'
text.capitalize()
'Hello how are you..??'
text.title()
'Hello How Are You..??'
text.swapcase()
'hELLO HOW ARE YOU..??'
text
'Hello how are you..??'
text.index('a')
10
text.index('o')
4
text.index('o',5)
7
text.index('o',8)
15
text.rindex('o')
15
text.find('o')
4
text.find('o',5)
7
text.index('z',8)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    text.index('z',8)
ValueError: substring not found
text.find('z',5)
-1
text.count('o')
3
text.count('o', 5)
2
text.startswith('a')
False
text.startswith('t')
False
text.startswith('H')
True
text.endswith('?')
True
text.isalnum()
False
text.islower()
False
text.isupper()
False
text.isdigit()
False
text.isnumeric()
False
text = "     Hello"

text.strip()
'Hello'
text.lstrip()
'Hello'
text = "###Hello..."
text.lstrip("#")
'Hello...'
>>> text
'###Hello...'
>>> text = text.lstrip("#")
>>> text = text.rstrip(".")
>>> text
'Hello'
>>> text = "Hello how are you ?"
>>> text.split()
['Hello', 'how', 'are', 'you', '?']
>>> text.replace('how', "where")
'Hello where are you ?'
>>> text
'Hello how are you ?'
