#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:40:34 2019

@author: sjdthree
"""

import sympy as sy

"""

from twitter:
    https://twitter.com/fermatslibrary/status/1192083979710713858
 11/6/2019, Kaprekar Numbers are numbers whose square in that base can be split into 2 parts that add up to the original number.

An example: 45 is a Kaprekar number, because 
45² = 2025 and 
20 + 25 = 45
9^2
45^2
297^2
7777^2
"""
"""
first some
Algebra:

x2 = 1000y+z
x = y+z
where y and z are three digits
and therefore x is at least 3 digits or more

x2 - x = 999y
x: 100 - 1999 -- that is max range if y & z are 3 digits

"""

def print_winner(x,digs):
    #digs = 
    print("\nwinner: ",x)
    xs = x*x
    topdigs = xs // 10**digs
    print("x^2 = ",xs, topdigs, xs - topdigs*10**digs) 
    print("Check: ",x, topdigs + xs - topdigs*10**digs)
    

if __name__ == '__main__':
    
    for digs in range(3,8):
        for xx in range(10**(digs-1),10**digs):
            rez = xx*xx-xx
            if sy.mod.Mod(rez,10**digs-1) == 0:
                print_winner(xx,digs)
        

