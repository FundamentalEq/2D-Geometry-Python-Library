from decimal import *
from Point import Point
import math

class Segment:
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
        return False

    # Check if the line segment contains the given point or not
    def contains(self,p) :
        pass
