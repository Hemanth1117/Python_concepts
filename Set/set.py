"""
SET({})
Sets are unordered collections of unique items.

Common Methods:
-add(x):
-remove(x):
-discard(x):
-union():
-intersection():
-difference():
-issubset():
-issuperset():
-symmetric_difference():
-pop():
-clear():


"""

#examples:
s = {1,2,3}
s.add(4) #{1,2,3,4}
s.remove(2) #{1,3,4}

#Set Comprehension
sc = {char for char in "hello"} #{'h','e','l','o'}