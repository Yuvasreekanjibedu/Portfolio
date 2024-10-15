Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={10,20,30,40,50,10,20,30}
>>> s
{50, 20, 40, 10, 30}
>>> s={'hai',99,23,10,23,11,34,'hai'}
>>> s
{34, 99, 'hai', 23, 10, 11}
>>> s={34,89,,(34),78,23}
SyntaxError: invalid syntax
>>> s={34,89,(34),78,23}
>>> s
{89, 34, 78, 23}
>>> s={34,89,(34,),78,23}
>>> s
{34, 23, (34,), 89, 78}
>>> #dictionary
