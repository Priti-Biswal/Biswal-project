class Point:
    # Documentation string
    """
       The class Point represents a #D point
       Instance attributes: x,y,z
    """
    #Default object initialization
    def __init__(self):
        self.mX = 1.1
        self.mY = 1.1
        self.mZ = 1.1
        print( "call FIRST\n")

    #Custom initialization
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.mX = x
        self.mY = y 
        self.mZ = z
        print( "call second\n")
		 #Print out the String of this object's values
    def toString(self):
        return '({}, {}, {})'.format(str(self.mX),str(self.mY),str(self.mZ))

    #Set new locations for the point
    def SetPoint(self, x=None, y=None, z=None):
        if x is not None:   #this is just a trick
            self.mX = x     #to only update values
        if y is not None:   #passed to function only
            self.mY = y
        if z is not None:
            self.mZ = z

    #Returns the distance
    def Distance(self, other):
        d = (( (other.mX - self.mX) ** 2) 
            + ((other.mY - self.mY) ** 2) 
            + ((other.mZ - self.mZ) ** 2)) ** 0.5
        return d


#Remember this method gets executed sinces its our 'main'
def main():
    p1 = Point()
    p2 = Point(4.0, 5.0, -2.0)
    p3 = Point(z = 3.0)

    print( p1.toString() )
    print( p2.toString() )
    print( p3.toString() )

if __name__ == "__main__":
    main()
	
(0.0, 0.0, 0.0)
(4.0, 5.0, -2.0)
(0.0, 0.0, 3.0)

