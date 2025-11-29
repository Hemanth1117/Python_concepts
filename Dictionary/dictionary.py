'''
DICTIONARY({})
Dictionaries are mutable collections of key-value pairs.


Common Methods:
-get(key):
-pop(key):
-popitem():
-update():
-keys():
-values():
-items():
-setdefault():
-clear():
-copy():

'''
#examples:
dic = {"a":1}
dic["b"] = 2
dic.get("a") # 1
dic.pop("b") # {"a":1}


#dictionary comprehension:
dc = {v: v**2 for v in range(3)}  #{0:0, 1:1, 2:4}