'''
STRINT("")
Strings are immutable sequences of characters.

Common Methods:
 -lower():
 -upper():
 -title():
 -capitalize():
 -replace(old, new):
 -split():
 -join():
 -strip():
 -lstrip():
 -rstrip():
 -startswith():
 -endswith():
 -find():
 -rfind():
 -index():
 -isalpha():
 -isdigit():
 -isspace():

'''

#example:
str = "Hello"
str.strip()  #"Hello"
str.upper()  #"HELLO"
"hello world".replace("world","python")
"-".join(['A', 'B']) #"A-B"



#Comperhension (via list):
[char.upper() for char in "abc"] # ['A', 'B', 'C']