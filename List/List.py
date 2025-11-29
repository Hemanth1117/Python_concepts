"""
List([])
Lists are mutable, ordered collections. They can hold elements of differents data types

Common Methods:
 . append(x): Add elements from iterable.
 . extend(iterable): Add elements from iterable.
 .insert(i, x): Insert x at index i.
 .pop([i]): Remove and return item at index i (default last).
 .remove(x): Remove first occurrence of x.
 .reverse():Reverse in-place.
 .sort(): Sort the list in-place.
 .index(x): Return the index of x.
 .count(x): Count occurrences.
 .clear(): Remove all elements.

"""
# example

l = [1, 2, 3, 4, 5]
l.append(6) # [1,2,3,4,5,6]
l.insert(0, 0) #[0,1,2,3,4,5,6]
l.remove(2) #[0,1,3,4,5,6]
l.sort() #[0,1,3,4,5,6]

print(l)



# List Comprehension:
cl1=[x ** 2 for x in range(5)] #[0, 1, 4, 9, 16]
cl2=[x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
print(cl1)
print(cl2)




# copy in list

# 11. copy()

# Returns a shallow copy of the list.

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]




# 2. extend(iterable)

# Adds all elements from another iterable (list, tuple, etc.).

a = [1, 2]
a.extend([3, 4])
print(a)  # [1, 2, 3, 4]