#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:01:09 2018

@author: wwt
"""
import itertools
a='ABC'
b=itertools.cycle(a)
for i in range(20):
    print(next(b))
            
            