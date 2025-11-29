"""
Comprehension Summary
"""
#List
List = [x for x in range(5)]
#Dict
Dict = {x:x**2 for x in range(5)}
#Set
Set = {x for x in "hello"}
#Tuple
Tuple = tuple(x for x in range(3))


"""
Best Use Cases:
List: ordered data with duplicates
Tuple: fixed and hashable sequences
Set: unique items, fast membership test
Dict: fast lookup for key-value


"""