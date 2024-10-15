Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='hai python'
s.isspace()
False
s2='j'
s2.isspace()
False
s3=' '
s3.isspace()
True
s='                                  yuva                                              '
s.strip()
'yuva'
s.lstrip()
'yuva                                              '
s.rstrip()
'                                  yuva'
s='hai python'
4
4
s.split('t)
        
SyntaxError: unterminated string literal (detected at line 1)
s.split('t')
        
['hai py', 'hon']
s.split('a')
        
['h', 'i python']
s.split('h')
        
['', 'ai pyt', 'on']
s.split('h',1)
        
['', 'ai python']
s.split('h',500)
        
['', 'ai pyt', 'on']
s.split('h',15)
        
['', 'ai pyt', 'on']
s.split('w')
        
['hai python']
s.split()
        
['hai', 'python']
s='hello hello'
        
s.split('l')
        
['he', '', 'o he', '', 'o']
#replace methood
        
#reolace(oldstring,newstring,[count])
        
#replace(oldstring,newstring,[count])
        
s='hai python'
        
s.replace("h','b')
          
SyntaxError: unterminated string literal (detected at line 1)
s.replace('h','b')
          
'bai pytbon'
s
          
'hai python'
s.replace('h','b',1)
          
'bai python'
s.replace('w','b')
          
'hai python'
s.replace('h','b').replace('b','h')
          
'hai python'
>>> s.replace('h','')
...           
'ai pyton'
>>> s.replace('h',' ')
...           
' ai pyt on'
>>> #count method
...           
>>> s.count('h',0,3)
...           
1
>>> s.count('h')
...           
2
>>> s,count('h',2)
...           
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s,count('h',2)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> s.count('h',2)
...           
1
>>> s.count('h',7)
...           
1
>>> s.count('h',2,7)
...           
0
>>> s,count('w')
...           
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s,count('w')
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> s.count('w')
...           
0
