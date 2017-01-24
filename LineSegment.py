from decimal import *
from Point import Point
import math

from GlobalValuesLib import *

class Segment:

    Origin = Point(0,0)

    def __init__(self,a,b) :

        if a.x < b.x :
            self.a = a
            self.b = b
        else :
            self.a = b
            self.b = a

        self.length = a.distance(b)
        self.points = (self.a,self.b)

        # finding slope of the line
        if abs(b.x - a.x) <= EPS :
            self.slope = Inf
        else :
            self.slope = (b.y - a.y)/(b.x - a.x)

    # Check if the two line segments ar
    def is_parallel(self,ls) :
        # if both are vertical lines
        if self.slope == Inf and ls.slope == Inf :
            return True
        # if one is vertical and other is not
        if self.slope == Inf or ls.slope == Inf :
            return False

        # the genral case
        if abs(self.slope - ls.slope) <= EPS :
            return True

        # Rotate the line segments and again check for the line segments to be parallel
        # to handle the case where the line segments are almost parallel but have very
        # large slope as they are vertical
        selfn = Segment(Origin.rotate(math.pi/2,self.a),Origin.rotate(math.pi/2,self.b))
        lsn = Segment(Origin.rotate(math.pi/2,ls.a),Origin.rotate(math.pi/2,ls.b))

        if abs(selfn.slope - lsn.slope) <= EPS :
            return True

        return False


    # Check if the line segment contains the given point "p" or not
    def contains(self,p) :
        if self.is_parallel(Segment(p,self.a)) :
            if p.distance(self.a) <= EPS or p.distance(self.b) <= EPS :
                return True
            if self.a.x <= p.x and p.x <= self.b.x :
                return True
        else :
            return False
