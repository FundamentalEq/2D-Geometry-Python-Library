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
        self.coordinates = (self.a,self.b)

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
        selfn = Segment(self.Origin.rotate(math.pi/2,self.a),self.Origin.rotate(math.pi/2,self.b))
        lsn = Segment(self.Origin.rotate(math.pi/2,ls.a),self.Origin.rotate(math.pi/2,ls.b))

        # if both are vertical lines
        if selfn.slope == Inf and lsn.slope == Inf :
            return True
        # if one is vertical and other is not
        if selfn.slope == Inf or lsn.slope == Inf :
            return False

        # the genral case
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

    # find the projection of the given point "p" on the line segment
    def projection(self,p) :
        # if the point itself lies on the line segment return the point
        if self.is_parallel(Segment(self.a,p)) :
            return p

        # shift self.Origin to a
        bn = Point(self.b.x - self.a.x,self.b.y - self.a.y)
        pn = Point(p.x - self.a.x ,p.y - self.a.y)

        # form the unit vector
        bn = Point(bn.x/self.Origin.distance(bn) , bn.y/self.Origin.distance(bn))

        # find dot product
        t = bn.x * pn.x + bn.y * pn.y

        # find the projected point
        ans = Point(t*bn.x,t*bn.y)

        # translate back the self.Origin
        ans = Point(ans.x + self.a.x,ans.y + self.a.y)

        return ans
        
    def intersect(self,ls):
        xdiff = (self.b.x - self.a.x,ls.b.x - ls.a.x)
        ydiff = (self.b.y - self.a.y,ls.b.y - ls.a.y)

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)

        if abs(div) <= EPS:
            raise Exception('lines do not intersect')

        d = (det(self.a.coordinates,self.b.coordinates), det(ls.a.coordinates,ls.b.coordinates))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return Point(-x,-y)
