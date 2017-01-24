from decimal import *
from Point import Point
import math

from GlobalValuesLib import *

class Segment:

    Origin = Point(0,0)

    def __init__(self,a,b) :
        self.a = a
        self.b = b
        self.length = a.distance(b)
        self.points = (a,b)
        # finding slope of the line
        if abs(b.x - a.x) <= EPS :
            self.slope = Inf
        else :
            self.slope = (b.y - a.y)/(b.x - a.x)

    # Check if the two line segments ar
    def is_parallel(self,ls) :
        if self.slope == Inf and ls.slope == Inf :
            return True
        if self.slope == Inf or ls.slope == Inf :
            return False

        if abs(self.slope - ls.slope) <= EPS :
            return True

        # Rotate the line segments and again check for the line segments to be parallel
        # to handle the case where the line segments are almost parallel but have very
        # large slope as they are vertical
        selfn = Segment(Origin.rotate(math.pi/2,self.a),Origin.rotate(math.pi/2,self.b))
        lsn = Segment(Origin.rotate(math.pi/2,ls.a),Origin.rotate(math.pi/2,ls.b))

        if selfn.slope == Inf and lsn.slope == Inf :
            return True
        if selfn.slope == Inf or lsn.slope == Inf :
            return False

        if abs(selfn.slope - lsn.slope) <= EPS :
            return True

        return False


    # Check if the line segment contains the given point or not
    def contains(self,p) :
        pass
