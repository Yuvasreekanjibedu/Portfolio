Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'1' in '123'
True
[1] in [2,3,1,4]
False
[1] in [2,3,[1],4]
True
'2' in '234'
True
(9,) in (9,8,7,6)
False



(9,) in (9,8,7,6)

False

(9,) in (9,8,7,6)

False
c=257
d=257
c is d
False
id(c)
1965831445776
id(d)
1965831445808
c==b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c==b
NameError: name 'b' is not defined
c==d
True
s='hai'
s1='hai'
s is s1
True
l=[11,22,33]
l1=[11,22,33]
l is l1
False
id(l)
1965837328896
id(l1)
1965793350400
t=(11,22,33)
t1=(11,22,33)
t is not t1
True
t is t1
False
t==t1
True
a=900
b=900
>>> a is b
False
>>> a is not b
True
>>> a==b
True
>>> a={90}
>>> b={90}
>>> a is b
False
>>> a==b
True
>>> a='mani'
>>> b='mani'
>>> a is not b
False
>>> a==b
True
>>> 10 and 20
20
>>> 10 and []
[]
>>> [] and ()
[]
>>> [] or 4
4
>>> {} and []
{}
>>> 2**3**2
512
>>> 5**2**1
25
>>> a=90
>>> a+=10
>>> a
100
>>> a-=50
>>> a
50
