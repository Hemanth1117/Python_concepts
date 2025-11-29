# built-in math related operations

# x = 3.14
# y = -4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(3, 4)
# result=max(x, y, z)
# result = min(x, y, z)

# print(result)



# if we need the pi value we need to import math module

import math
# x = 9.1
# # print(math.pi)
# # print(math.e)
# # result = math.sqrt(x)
# # result = math.ceil(x)
# result = math.floor(x)
# print(result)






# exercise on circumference


# radius = float(input("Enter the radius of a circle: "))
# circumfernce = 2 * math.pi * radius
# print(f"The circumference is:{round(circumfernce, 2)}cm")


# exercise on area of circle

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)}cm^2")




# hypothesis of a rightriangle

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side c ={round(c, 2)}")