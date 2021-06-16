#!/usr/bin/python
def ref_demo(x):
    print ("x=",x ) 
    print ("id Of X = ",id(x))
    x=42
    print ("x=",x ) 
    print ("id Of X = ",id(x))

x=9;
ref_demo(x)
print ("x=",x ) 
print ("id Of X = ",id(x))

