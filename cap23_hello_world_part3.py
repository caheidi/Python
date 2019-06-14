Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = "part one"
>>> B = "part two"
>>> +
SyntaxError: invalid syntax
>>> 
>>> A+B
'part onepart two'
>>> A = "PART A"
>>> B= 1
>>> A+B
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    A+B
TypeError: can only concatenate str (not "int") to str
>>> A+str(B)
'PART A1'
>>> "{}-{}".format(A,B)
'PART A-1'
>>> A="Hola"
>>> B="Silvia"
>>> C=1
>>> A+B+str(C)
'HolaSilvia1'
>>> "{}-{}".format(A,B,C)
'Hola-Silvia'
>>> "{}-{}-{}".format(A,B,C)
'Hola-Silvia-1'
>>> 
