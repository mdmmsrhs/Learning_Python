#!/bin/Python

"""define a class called Point and initialise it"""

class Point:
	def __init__(self, x=0, y=0):
		    self.x = x
		    self.y = y
		    
		    
def printPoint(p):
	print'(' + str(p.x) + ',' + str(p.y) + ')'

def samePoint(p1,p2):
	return (p1.x == p2.x) and (p1.y == p2.y)
	
def	distanceSquared(p):
	return (p.x * p.x) + (p.y * p.y)
	
"""Instantiate a Point"""

blank = Point()
print(blank.x,blank.y)

#distanceSquared = (blank.x * blank.x) + (blank.y * blank.y)

print(distanceSquared(blank))


blank.x = 8
blank.y = 9

print(blank.x,blank.y)

print(distanceSquared(blank))

printPoint(blank)

p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = Point()
p2.x = 3.0
p2.y = 4.0

print(samePoint(p1,p2))

######################################

class Rectangle():
	pass
		    
def findCentre(r):
	p = Point()
	p.x = r.corner.x = r.width/2
	p.y = r.corner.y = r.height/2
	return p
	
box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

centre = findCentre(box)
print("The centre of the rectagle is: \n")
printPoint(centre)

#end