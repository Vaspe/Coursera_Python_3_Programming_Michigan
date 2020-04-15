# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:30:25 2020

@author: Vasilis

In Python, every value is actually an object. Whether it be a dictionary, a list, 
or even an integer, they are all objects. Programs manipulate those objects either
by performing computation with them or by asking them to perform methods. To be 
more specific, we say that an object has a state and a collection of methods that
it can perform. (More about methods below.) The state of an object represents 
those things that the object knows about itself. The state is stored in instance
variables. 

Nice general doc:
    https://www.w3schools.com/python/python_classes.asp

Dunderscore possibiliteies and keywords for classes:
    http://www.siafoo.net/article/57    
"""

#%% Defining a class
# __init__(self) is always required to initializa a class!It is called the construcotr

class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    
    printed_rep = "*"  # I am a class variable!
    def __init__(self,initX=0,initY=0):

        self.x = initX # initializing values of the instance variables (instance bcause it has a dot!)
        self.y = initY # initializing values of the instance variables (instance bcause it has a dot!)
    def getX(self):
        return self.x 
    def getY(self):
        return self.y    
    def distanceFromOrigin(self):
        dist = (self.x**2 + self.y**2)**0.5
        return dist
    def distance(self,p2):
        distance1 = ( (self.getX()-p2.getX())**2 + (self.getY()-p2.getY())**2 ) **0.5
        return distance1
    
    # we can also include a method called __str___ which will be used automatically when
    # the print funvtion is called and will print as string the state of the object  
    def __str__(self):
        return ('x = ' + str(self.x) + ' y = ' + str(self.y))
    
    # Adding some standard __dunderscore__ methods
    # http://www.siafoo.net/article/57     
    def __add__(self, p2):
        p3 = Point(self.x + p2.x,self.y + p2.y)
        return p3
    
    def __sub__(self,other):
        p3 = Point(self.x - p2.x , self.y - p2.y)
        return p3
    
    # definig other methods that generate an object instamce of our class
    def halfway(self,p2):
        midpnt = Point( (self.x + p2.x)/2 , (self.y + p2.y)/2 )
        return midpnt

    # simplified text based graph demonstrating a class variable that is seen from all objects
    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)    


#%% Testin'
p = Point()   # Instantiate an object of type Point
q = Point()   # and make a second Point instance totally unconnected to the previous, like turtles!

print(p)
print(type(p))
print(type(Point))
print(p is q)
print(p.x)
p.x = 150
print(p.x)
print(q.x)
q.z = 0
print(q.z)
print(p.getX())
print('------------------------------------')
k = Point(7,6)
print(k.x)
print(k.y)
print(k.getX()) # this is exaclty the same with k.x but using the get we make sure we dont change the variable by mistake
print(k.distanceFromOrigin())
print('------------------------------------')
p3 = p+q # now p3 is a new instance of the classe point and it is an independent object
print('Adding the poins p+q with the __add__ method yield the point (' + str(p3.getX())+','+ str(p3.getY())+ ')')
#print(p.z) # Gives an error becuase it is not defined!
print('------------------------------------')
p4 = p.halfway(q)
print(p4)
print('The midpoint between p and q using the halfway method is: (' + str(p4.getX())+','+ str(p4.getY())+ ')')
print('------------------------------------')


#%% Ican use the instances assigned to variables as regular variables for other functions
def distance(p1,p2):
    ''' eukledian distance of teo points'''
    distance = ( (p1.getX()-p2.getX())**2 + (p1.getY()-p2.getY())**2 ) **0.5
    return distance
    
print('The distance between points p and q is ' + str(distance(q,p)) )
print('------------------------------------')
# alternatively if it makes semantically sense we could add this as a method of the point class 
# see above impolementation. The choice is more about taste and conception!
print('The distance of point q from p is ' + str(p.distance(q)) )
print('------------------------------------')
#%% Example again
class NumberSet:
    ''' Some text to define the class'''
    def __init__(self,InitNum1 = 0, InitNum2 = 0):
        self.num1 = InitNum1
        self.num2 = InitNum2

t = NumberSet(6,10) 
print(t.num2)

print('------------------------------------')

#%% Anothe Example!
class Animal:
    def __init__(self,init_arms=2,init_legs=2):
        self.arms = init_arms
        self.legs = init_legs
    def limbs(self):
        return self.arms+self.legs
    
spider = Animal(4,4)    
spidlimbs = spider.limbs()

print(spidlimbs)
print('------------------------------------')

#%% One more example here:
class Cereal:
    def __init__(self,initName = 'All bran',initBrand = 'Kellogs', initFiber = 10):
        self.name = initName
        self.brand = initBrand
        self.fiber = initFiber
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber)

c1= Cereal("Corn Flakes","Kellogg's",2)
c2 = Cereal("Honey Nut Cheerios","General Mills",3)
print(c1)
print(c2)
print('---------------------------------------')

#%% class objects can be sorted exactly in the same way as the other objects:
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def sort_priority(self):
        return self.price
    
L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)
L2 = sorted(L, key = lambda x:x.price)
L3 =  [x.name for x in L2]
# or to simplify we can add a method that return a shorting values inside the class
L4 = [x. name for x in sorted(L, key = Fruit.sort_priority)]
print('---------------------------------------')

#%% we can also define class variable
'''
Class variables are defined after class keyword and before the __init__ constructor
They are only seen internally in the class by all methods. These variables cannot 
be set outside the class definition!
''' 
p11 = Point(2, 3)
p12 = Point(3, 12)
print(p11.graph())
print()
print(p12.graph())
print(p11.printed_rep)
print('---------------------------------------')

#%% Scoping a class 
'''
- What is the data that you want to deal with?
- What will one instance of your class represent?
- What information should each instance have as instance variables?
- What instance methods should each instance have?
- What should the printed version of an instance look like? 
'''










