"""
TUPLE(())
Tuples are immutable sequences. Useful when data should not change

Common Methods:
.count(x): Count occurrences.
.index(x): Find index.

"""
#examples:
tup = (1, 2, 2, 3)
tup.count(2) #2
tup.index(3) #3


#Comprehension:
tuple(x**2 for x in range(3)) #(0, 1, 4)