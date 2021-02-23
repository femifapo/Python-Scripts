# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:58:12 2020

@author: Dell
"""

import cv2 as cv 

def testDevice(source):
   cap = cv.VideoCapture(source)
   if cap is None or not cap.isOpened():
       cap.open(1)
       
   if cap.isOpened():
       print('cam is now opened')      
       
   if cv.waitkey(1) & 0xFF == ord('q'):
       break
   
cap.release()
cv.destroyAllWindows()
       