from graphics import rectangle
from graphics import circle

from Dgraphics import *  #import cuboid and sphere

print("Read values: \n Rectangle:\n")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
r_area=rectangle.area(l,b)
r_perimeter=rectangle.perimeter(l,b)


print("Circle:\n")
r=int(input("Enter radius"))
area=circle.area(circle.pi,r)
perimeter=circle.perimeter(circle.pi,r)

print("Read values: \n Cuboid:\n")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
h=int(input("Enter height"))
c_area=cuboid.area(l,b,h)
c_perimeter=cuboid.perimeter(l,b,h)

print("Read values: \n Sphere:\n")
r=int(input("Enter radius"))
sphere_surf_area=sphere.surf_area(sphere.pi,r)
sphere_circumference=sphere.circumference(sphere.pi,r)
sphere_volume=sphere.sphere_volume(sphere.pi,r)

print("Area of Rectangle:",r_area)
print("Perimeter of Rectangle:",r_perimeter)

print("Area of Circle:",area)
print("Perimeter of Circle:",perimeter)



print("Area of cuboid:",c_area)
print("Perimeter of cuboid:",c_perimeter)

print("surface Area of sphere:",sphere_surf_area)
print("circumference of sphere:",sphere_circumference)
print("sphere_volume:",sphere_volume)

