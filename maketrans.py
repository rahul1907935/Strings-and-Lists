# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 12:03:59 2021

@author: rahul
"""

txt = "Hello Raj!"
mytable = txt.maketrans("R", "T")
print(txt.translate(mytable))