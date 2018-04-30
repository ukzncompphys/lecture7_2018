import numpy
class vector:
    def __init__(self,x):
        self.data=x
    def sum(self):
        return numpy.sum(self.data)

class Complex:
    def __init__(self,r=0.0,i=0.0):
        self.r=r
        self.i=i
    def abs(self):
        y=numpy.sqrt(self.r**2+self.i**2)
        return y
        
