# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:26:11 2021

@author: rahul
"""

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))