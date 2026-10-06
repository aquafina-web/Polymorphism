#method overloading polymorphism
# this code doesn't work for python

class Shape:
    def area(self,r):
        return 3.14 * r * r
    def area (self,l,b):
        return l * b
    
s1 = Shape()
s1.area(2)
s1.area(3,4)    

class Shape:
    def area(self,l,b=0):
        #circle
        if b == 0 :
            return 3.14 * l * l;
        #rectangle
        else:
            return l * b
        
    
s1 = Shape()
print(s1.area(5))
print(s1.area(5,6))
