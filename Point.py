from decimal import *
import math

class Point :
    # init the point
    def __init__(self,x,y) :
        self.x = Decimal(x)
        self.y = Decimal(y)

    # mid point between self and the other point
    def midpoint(self,other) :
        return Point((self.x+other.x)/2,(self.y+other.y)/2)

    # distance of the self from the other point
    def distance(self,other) :
        return Decimal( math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) )

    # rotate the argument by point by argument theta in clock wise direction
    def rotate(self,theta,other) :
        # translate to shift origin
        other.x -= self.x
        other.y -= self.y

        # perform rotation about origin
        ans = Point( other.x*Decimal( math.cos(theta) ) - other.y*float( math.sin(theta) ),
                     other.x*Decimal( math.sin(theta) ) + other.y*Decimal( math.cos(theta) ) )

        # translate back to restore origin
        ans.x += self.x
        ans.y += self.y
        return ans
