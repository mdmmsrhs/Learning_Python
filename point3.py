#!/bin/Python

"""
    define a class called Point and initialise it
    rewritten in a more OOP style
"""

class Point:
    def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
            
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def __add__(self,other):
        return Point((self.x + other.x), (self.y + other.y))
        
    def __mul__(self,other):
        return self.x * other.x + self.y * other.y
        
    def __rmul__(self,other):
        return Point(other * self.x, other * self.y)
        
def main():
    p = Point(3,4)
    print p
    test = 3+4
    print test
    p1 = Point(3,4)
    p2 = Point(5,7)
    p3 = p1 + p2
    print p1, p2, p3
    print p1 * p2
    print 2 * p2
    print 2 * p1

if __name__ == '__main__':
    # execute only if run as a script
    main()