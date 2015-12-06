#!/bin/python

import math

"""distance function from section 5.2"""
"""Pythagorean theorem: distance (between two points) = sqrt((x2-x1)^2 + y2-y1)^2)"""

def distance(x1,x2,y1,y2):
	dx = x2-x1
	dy = y2-y1
	dist = math.sqrt((dx**2) + (dy**2))
	return dist

print "the distance between point1 and point2 is: ", distance(2.0,4.0,4.0,5.0), " units.\n"
