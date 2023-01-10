# import math allows the use of math.sqrt
import math
# get the input
x1 = float(input("Enter x1 value: "))
y1 = float(input("Enter y1 value: "))
x2 = float(input("Enter x2 value: "))
y2 = float(input("Enter y2 value: "))
# math
d = str(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1)**2)))
# output
print("The distance is " + d)
