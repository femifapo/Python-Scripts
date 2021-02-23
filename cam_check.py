# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:10:42 2020

@author: Dell
"""

import cv2 as cv 

def testDevice(source):
   cap = cv.VideoCapture(source) 
   if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)
       print(source)

testDevice(0) # no printout
testDevice(1) # prints message