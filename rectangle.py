#!/bin/python

class Point():
	pass

def printPoint(p):
	print'(' + str(p.x) + ',' + str(p.y) + ')'

def samePoint(p1,p2):
	return (p1.x == p2.x) and (p1.y == p2.y)
	
def	distancesquared(p):
	return (p.x * p.x) + (p.y * p.y)

#########################################################################################
	
class Rectangle():
	def __init__(self):
		    self.width = 30
		    self.height = 40
		    
def findCentre(r):
	p = Point()
	p.x = r.corner.x + (r.width/2.0)
	p.y = r.corner.y + (r.height/2.0)
	return p
	
#def growRect(r,dwidth,dheight):
#	r.width = r.width + dwidth
#	r.height = r.height+dheight
		
#def moveRect(r,dx,dy):
#	r.corner.x = r.corner.x + dx
#	r.corner.y = r.corner.y + dy
	
		
def growRect(r,dwidth,dheight):
	import copy
	p = copy.deepcopy(r)
	p.width = p.width + dwidth
	p.height = p.height + dheight
	return p
	
def moveRect(r,dx,dy):
	import copy
	p = copy.deepcopy(r)
	p.corner.x = p.corner.x + dx
	p.corner.y = p.corner.y + dy
	return p		

######################################################################################
	
box = Rectangle()
box.width = 100.0
box.height = 200.0

print "Rectangle:"

print "Width: ",box.width
print "Height: ",box.height

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print "Lower left corner is at: " 
printPoint(box.corner)

print "Rectangle centre is at: "
printPoint(findCentre(box))
print "\n"

box2 = growRect(box,30.0,50.0)

print "After growth:"

print "New width: ",box2.width
print "New height: ",box2.height

print "Rectangle centre after growth is now at: "
printPoint(findCentre(box2))
print "\n"

box3=moveRect(box,10.0,10.0)

print "After translation"

print "New width: ",box3.width
print "New height: ",box3.height

print "Lower left corner after translation is now at: "
printPoint(box3.corner)

print "Rectangle centre after translation is now at: "
printPoint(findCentre(box3))

#end