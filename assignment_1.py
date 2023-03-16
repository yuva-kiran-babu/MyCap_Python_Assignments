# Task number 1 calculating the radius of a circle:

radius=float(input("Input the radius of circle : "))
from math import *
area=pi*radius**2
print("The area of the circle with radius "+str(radius)+" is "+str(area))


# Task number 2 writing the extension of the file:

file_name=input("Input the file name: ")
if ".py" in file_name:
    print("The extension of the file is 'python'") 

elif ".cpp" in file_name:
    print("The extension of the file is 'c++'")

elif ".c" in file_name:
    print("The extension of the file is 'c'")



