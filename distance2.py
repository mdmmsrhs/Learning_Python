#!/bin/python

"""A rewrite of the distance class using points instead"""

class Point:
	def __init__(self):
		    self.x = 3
		    self.y = 4
		    
import math		    
		    
"""Pythagorean theorem: distance (between two points) = sqrt((x2-x1)^2 + y2-y1)^2)"""

def distance(p1,p2):
	dx = p2.x-p1.x
	dy = p2.y-p1.y
	dist = math.sqrt((dx**2) + (dy**2))
	return dist

point1 = Point()
point1.x = 2.0
point1.y = 3.0

point2 = Point()
point2.x = 5.0
point2.y = 7.0

print "the distance between point1 and point2 is: ", distance(point1,point2), " units.\n"

#end
