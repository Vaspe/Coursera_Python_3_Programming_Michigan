# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:45:16 2020

@author: Vasilis
"""

#%% Ex1
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

circ,area= circleInfo(10)
print("area is " + str(area))
print("circumference is " + str(circ))


#%% Ex2
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

people = [julia, claude, alan]
for i in people:
    print(i[1]+ ", " + str(i[2]) + ", " + i[3] )
    
#%% Ex 3
    
    








